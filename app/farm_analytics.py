from sqlalchemy.orm import Session
from sqlalchemy import func, and_, extract
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from app import models, schemas, crud

class FarmAnalyticsService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_farm_dashboard(self, farm_id: int) -> schemas.FarmAnalytics:
        """Çiftlik dashboard verilerini getirir"""
        
        # Toplam hayvan sayısı
        total_animals = self.db.query(models.Animal).filter(
            and_(
                models.Animal.farm_id == farm_id,
                models.Animal.status == "active"
            )
        ).count()
        
        # Bu ayki üretim
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        monthly_production = self.db.query(
            func.sum(models.ProductionRecord.quantity)
        ).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                extract('month', models.ProductionRecord.record_date) == current_month,
                extract('year', models.ProductionRecord.record_date) == current_year
            )
        ).scalar() or 0
        
        # Bu ayki gelir
        monthly_income = self.db.query(
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "income",
                extract('month', models.FinancialRecord.record_date) == current_month,
                extract('year', models.FinancialRecord.record_date) == current_year
            )
        ).scalar() or 0
        
        # Bu ayki gider
        monthly_expenses = self.db.query(
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "expense",
                extract('month', models.FinancialRecord.record_date) == current_month,
                extract('year', models.FinancialRecord.record_date) == current_year
            )
        ).scalar() or 0
        
        # Kâr
        profit = monthly_income - monthly_expenses
        
        # Yaklaşan aşılar
        upcoming_vaccinations = len(crud.get_upcoming_vaccinations(self.db, farm_id, 30))
        
        # Geciken sağlık kontrolleri
        overdue_health_checks = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.next_due_date < datetime.now(),
                models.HealthRecord.status == "pending"
            )
        ).count()
        
        # Günlük ortalama süt üretimi (sadece sığır için)
        daily_milk_avg = self.db.query(
            func.avg(models.ProductionRecord.quantity)
        ).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                models.ProductionRecord.production_type == "milk",
                models.ProductionRecord.record_date >= datetime.now() - timedelta(days=30)
            )
        ).scalar()
        
        # Hayvan başına yem maliyeti
        total_feed_cost = self.db.query(
            func.sum(models.FeedRecord.total_cost)
        ).filter(
            and_(
                models.FeedRecord.farm_id == farm_id,
                models.FeedRecord.feed_date >= datetime.now() - timedelta(days=30)
            )
        ).scalar() or 0
        
        feed_cost_per_animal = total_feed_cost / total_animals if total_animals > 0 else 0
        
        return schemas.FarmAnalytics(
            total_animals=total_animals,
            total_production_this_month=monthly_production,
            total_income_this_month=monthly_income,
            total_expenses_this_month=monthly_expenses,
            profit_this_month=profit,
            upcoming_vaccinations=upcoming_vaccinations,
            overdue_health_checks=overdue_health_checks,
            average_daily_milk_production=daily_milk_avg,
            feed_cost_per_animal=feed_cost_per_animal
        )
    
    def get_production_summary(self, farm_id: int, period: str = "monthly") -> schemas.ProductionSummary:
        """Üretim özetini getirir"""
        
        # Dönem hesaplama
        if period == "daily":
            start_date = datetime.now() - timedelta(days=1)
        elif period == "weekly":
            start_date = datetime.now() - timedelta(weeks=1)
        elif period == "monthly":
            start_date = datetime.now() - timedelta(days=30)
        elif period == "yearly":
            start_date = datetime.now() - timedelta(days=365)
        else:
            start_date = datetime.now() - timedelta(days=30)
        
        # Toplam üretim
        total_quantity = self.db.query(
            func.sum(models.ProductionRecord.quantity)
        ).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                models.ProductionRecord.record_date >= start_date
            )
        ).scalar() or 0
        
        # Toplam değer
        total_value = self.db.query(
            func.sum(models.ProductionRecord.total_value)
        ).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                models.ProductionRecord.record_date >= start_date
            )
        ).scalar() or 0
        
        # Hayvan başına ortalama
        total_animals = self.db.query(models.Animal).filter(
            and_(
                models.Animal.farm_id == farm_id,
                models.Animal.status == "active"
            )
        ).count()
        
        average_per_animal = total_quantity / total_animals if total_animals > 0 else 0
        
        # Trend hesaplama (basit karşılaştırma)
        previous_period_start = start_date - (start_date - datetime.now())
        previous_quantity = self.db.query(
            func.sum(models.ProductionRecord.quantity)
        ).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                models.ProductionRecord.record_date >= previous_period_start,
                models.ProductionRecord.record_date < start_date
            )
        ).scalar() or 0
        
        if previous_quantity > 0:
            if total_quantity > previous_quantity * 1.05:
                trend = "increasing"
            elif total_quantity < previous_quantity * 0.95:
                trend = "decreasing"
            else:
                trend = "stable"
        else:
            trend = "stable"
        
        return schemas.ProductionSummary(
            period=period,
            total_quantity=total_quantity,
            total_value=total_value,
            average_per_animal=average_per_animal,
            trend=trend
        )
    
    def get_health_summary(self, farm_id: int) -> schemas.HealthSummary:
        """Sağlık özetini getirir"""
        
        # Toplam aşı sayısı
        total_vaccinations = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.record_type == "vaccination"
            )
        ).count()
        
        # Bekleyen aşılar
        pending_vaccinations = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.record_type == "vaccination",
                models.HealthRecord.status == "pending"
            )
        ).count()
        
        # Geciken aşılar
        overdue_vaccinations = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.record_type == "vaccination",
                models.HealthRecord.next_due_date < datetime.now(),
                models.HealthRecord.status == "pending"
            )
        ).count()
        
        # Toplam tedavi sayısı
        total_treatments = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.record_type == "treatment"
            )
        ).count()
        
        # Aktif sağlık sorunları
        active_health_issues = self.db.query(models.HealthRecord).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.record_type == "disease",
                models.HealthRecord.status == "pending"
            )
        ).count()
        
        # Sonraki tarihler
        next_due_dates = self.db.query(models.HealthRecord.next_due_date).filter(
            and_(
                models.HealthRecord.farm_id == farm_id,
                models.HealthRecord.next_due_date >= datetime.now(),
                models.HealthRecord.status == "pending"
            )
        ).limit(5).all()
        
        next_dates = [date[0] for date in next_due_dates if date[0]]
        
        return schemas.HealthSummary(
            total_vaccinations=total_vaccinations,
            pending_vaccinations=pending_vaccinations,
            overdue_vaccinations=overdue_vaccinations,
            total_treatments=total_treatments,
            active_health_issues=active_health_issues,
            next_due_dates=next_dates
        )
    
    def get_financial_summary(self, farm_id: int, period_days: int = 30) -> schemas.FinancialSummary:
        """Finansal özeti getirir"""
        
        start_date = datetime.now() - timedelta(days=period_days)
        
        # Toplam gelir
        total_income = self.db.query(
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "income",
                models.FinancialRecord.record_date >= start_date
            )
        ).scalar() or 0
        
        # Toplam gider
        total_expenses = self.db.query(
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "expense",
                models.FinancialRecord.record_date >= start_date
            )
        ).scalar() or 0
        
        # Net kâr
        net_profit = total_income - total_expenses
        
        # Kategori bazında gelir
        income_by_category = {}
        income_categories = self.db.query(
            models.FinancialRecord.category,
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "income",
                models.FinancialRecord.record_date >= start_date
            )
        ).group_by(models.FinancialRecord.category).all()
        
        for category, amount in income_categories:
            income_by_category[category] = amount
        
        # Kategori bazında gider
        expenses_by_category = {}
        expense_categories = self.db.query(
            models.FinancialRecord.category,
            func.sum(models.FinancialRecord.amount)
        ).filter(
            and_(
                models.FinancialRecord.farm_id == farm_id,
                models.FinancialRecord.record_type == "expense",
                models.FinancialRecord.record_date >= start_date
            )
        ).group_by(models.FinancialRecord.category).all()
        
        for category, amount in expense_categories:
            expenses_by_category[category] = amount
        
        # Kâr marjı
        profit_margin = (net_profit / total_income * 100) if total_income > 0 else 0
        
        return schemas.FinancialSummary(
            total_income=total_income,
            total_expenses=total_expenses,
            net_profit=net_profit,
            income_by_category=income_by_category,
            expenses_by_category=expenses_by_category,
            profit_margin=profit_margin
        )
    
    def get_animal_performance(self, farm_id: int, animal_id: Optional[int] = None) -> Dict:
        """Hayvan performansını analiz eder"""
        
        if animal_id:
            # Belirli bir hayvan için
            animal = crud.get_animal(self.db, animal_id)
            if not animal or animal.farm_id != farm_id:
                return {}
            
            # Hayvanın üretim kayıtları
            production_records = crud.get_animal_production_records(self.db, animal_id, limit=30)
            
            # Hayvanın sağlık kayıtları
            health_records = crud.get_animal_health_records(self.db, animal_id, limit=10)
            
            # Performans hesaplama
            total_production = sum(record.quantity for record in production_records)
            avg_daily_production = total_production / len(production_records) if production_records else 0
            
            # Sağlık durumu
            recent_health_issues = len([r for r in health_records if r.record_type == "disease"])
            
            return {
                "animal_id": animal_id,
                "tag_number": animal.tag_number,
                "name": animal.name,
                "species": animal.species,
                "total_production": total_production,
                "average_daily_production": avg_daily_production,
                "recent_health_issues": recent_health_issues,
                "last_health_check": health_records[0].record_date if health_records else None
            }
        else:
            # Tüm hayvanlar için
            animals = crud.get_farm_animals(self.db, farm_id)
            animal_performance = []
            
            for animal in animals:
                performance = self.get_animal_performance(farm_id, animal.id)
                if performance:
                    animal_performance.append(performance)
            
            return {
                "total_animals": len(animals),
                "animal_performance": animal_performance
            }
    
    def get_feed_efficiency(self, farm_id: int, days: int = 30) -> Dict:
        """Yem verimliliğini analiz eder"""
        
        start_date = datetime.now() - timedelta(days=days)
        
        # Yem kayıtları
        feed_records = self.db.query(models.FeedRecord).filter(
            and_(
                models.FeedRecord.farm_id == farm_id,
                models.FeedRecord.feed_date >= start_date
            )
        ).all()
        
        # Toplam yem miktarı ve maliyeti
        total_feed_quantity = sum(record.quantity for record in feed_records)
        total_feed_cost = sum(record.total_cost or 0 for record in feed_records)
        
        # Üretim kayıtları
        production_records = self.db.query(models.ProductionRecord).filter(
            and_(
                models.ProductionRecord.farm_id == farm_id,
                models.ProductionRecord.record_date >= start_date
            )
        ).all()
        
        total_production = sum(record.quantity for record in production_records)
        
        # Yem verimliliği (kg yem / kg üretim)
        feed_efficiency = total_feed_quantity / total_production if total_production > 0 else 0
        
        # Yem maliyeti per kg üretim
        feed_cost_per_production = total_feed_cost / total_production if total_production > 0 else 0
        
        return {
            "total_feed_quantity": total_feed_quantity,
            "total_feed_cost": total_feed_cost,
            "total_production": total_production,
            "feed_efficiency": feed_efficiency,
            "feed_cost_per_production": feed_cost_per_production,
            "period_days": days
        }


