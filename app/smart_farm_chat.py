from sqlalchemy.orm import Session
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import re
from app import models, crud, schemas
from app.farm_analytics import FarmAnalyticsService

class SmartFarmChatService:
    def __init__(self, db: Session):
        self.db = db
        self.analytics_service = FarmAnalyticsService(db)
    
    def process_farm_query(self, user_id: int, query: str, farm_id: Optional[int] = None) -> Dict[str, Any]:
        """Çiftlik sorgusunu işler ve yanıt üretir"""
        
        # Kullanıcının çiftliklerini al
        if not farm_id:
            farms = crud.get_user_farms(self.db, user_id)
            if not farms:
                return {
                    "response": "Henüz kayıtlı çiftliğiniz bulunmuyor. Önce bir çiftlik eklemeniz gerekiyor.",
                    "suggestions": ["Çiftlik ekle", "Yardım al"]
                }
            farm_id = farms[0].id  # İlk çiftliği kullan
        
        # Sorgu analizi
        query_analysis = self._analyze_query(query)
        
        # Sorgu türüne göre yanıt üret (vet_appointment en başta, üretimle karışmasın)
        if query_analysis["type"] == "vet_appointment":
            return self._get_vet_appointments_response(farm_id)
        if query_analysis["type"] == "dashboard":
            return self._get_dashboard_response(farm_id)
        elif query_analysis["type"] == "production":
            return self._get_production_response(farm_id, query_analysis)
        elif query_analysis["type"] == "health":
            return self._get_health_response(farm_id, query_analysis)
        elif query_analysis["type"] == "financial":
            return self._get_financial_response(farm_id, query_analysis)
        elif query_analysis["type"] == "animal":
            return self._get_animal_response(farm_id, query_analysis)
        elif query_analysis["type"] == "feed":
            return self._get_feed_response(farm_id, query_analysis)
        else:
            return self._get_general_response(farm_id, query)
    
    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Sorguyu analiz eder ve türünü belirler.
        Veteriner randevusu en başta yakalanır (üretim raporu çıkmasın diye).
        """
        query_lower = query.lower().strip()
        
        # Veteriner randevusu / randevu sorguları (en önce; kesinlikle üretim dönmesin)
        if "veteriner" in query_lower or "randevu" in query_lower:
            return {"type": "vet_appointment", "keywords": ["veteriner", "randevu"]}
        
        # Sağlık sorguları (dashboard'dan önce)
        health_keywords = ["sağlık", "aşı", "hastalık", "tedavi", "kontrol"]
        if any(keyword in query_lower for keyword in health_keywords):
            return {"type": "health", "keywords": health_keywords}
        
        # Dashboard sorguları ("durum" burada; böylece "Sağlık durumu" yukarıda health'e gider)
        dashboard_keywords = ["özet", "genel durum", "dashboard", "ana sayfa", "durum", "nasıl"]
        if any(keyword in query_lower for keyword in dashboard_keywords):
            return {"type": "dashboard", "keywords": dashboard_keywords}
        
        # Üretim sorguları (hayvan başına performans → üretim raporu)
        production_keywords = ["üretim", "süt", "et", "yumurta", "yün", "miktar", "verim", "performans"]
        if any(keyword in query_lower for keyword in production_keywords):
            return {"type": "production", "keywords": production_keywords}
        
        # Finansal sorguları
        financial_keywords = ["gelir", "gider", "kâr", "maliyet", "para", "fiyat", "satış"]
        if any(keyword in query_lower for keyword in financial_keywords):
            return {"type": "financial", "keywords": financial_keywords}
        
        # Hayvan sorguları (liste, detay, ekle/güncelle; performans yukarıda üretimde)
        animal_keywords = ["hayvan", "sığır", "koyun", "keçi", "tavuk", "küpe", "numara"]
        if any(keyword in query_lower for keyword in animal_keywords):
            return {"type": "animal", "keywords": animal_keywords}
        
        # Yem sorguları
        feed_keywords = ["yem", "beslenme", "yem maliyeti", "yem verimliliği"]
        if any(keyword in query_lower for keyword in feed_keywords):
            return {"type": "feed", "keywords": feed_keywords}
        
        return {"type": "general", "keywords": []}
    
    def _get_dashboard_response(self, farm_id: int) -> Dict[str, Any]:
        """Dashboard yanıtı üretir"""
        
        analytics = self.analytics_service.get_farm_dashboard(farm_id)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"🏡 **{farm.name} Çiftliği Genel Durumu**\n\n"
        
        # Temel bilgiler
        response += f"📊 **Temel Bilgiler:**\n"
        response += f"• Toplam hayvan sayısı: {analytics.total_animals}\n"
        response += f"• Bu ayki üretim: {analytics.total_production_this_month:.1f} birim\n"
        response += f"• Bu ayki gelir: {analytics.total_income_this_month:.2f} TL\n"
        response += f"• Bu ayki gider: {analytics.total_expenses_this_month:.2f} TL\n"
        response += f"• Bu ayki kâr: {analytics.profit_this_month:.2f} TL\n\n"
        
        # Uyarılar
        if analytics.upcoming_vaccinations > 0:
            response += f"⚠️ **Uyarılar:**\n"
            response += f"• {analytics.upcoming_vaccinations} hayvanın aşı tarihi yaklaşıyor\n"
        
        if analytics.overdue_health_checks > 0:
            response += f"• {analytics.overdue_health_checks} hayvanın sağlık kontrolü gecikmiş\n"
        
        # Öneriler
        suggestions = []
        if analytics.profit_this_month < 0:
            suggestions.append("Giderleri azaltma önerileri")
        if analytics.upcoming_vaccinations > 0:
            suggestions.append("Aşı programı")
        if analytics.overdue_health_checks > 0:
            suggestions.append("Sağlık kontrolü planı")
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {
                "total_animals": analytics.total_animals,
                "monthly_production": analytics.total_production_this_month,
                "monthly_income": analytics.total_income_this_month,
                "monthly_expenses": analytics.total_expenses_this_month,
                "profit": analytics.profit_this_month
            }
        }
    
    def _get_production_response(self, farm_id: int, query_analysis: Dict) -> Dict[str, Any]:
        """Üretim yanıtı üretir"""
        
        production_summary = self.analytics_service.get_production_summary(farm_id, "monthly")
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"📈 **{farm.name} Üretim Raporu**\n\n"
        
        response += f"📊 **Bu Ayki Üretim:**\n"
        response += f"• Toplam miktar: {production_summary.total_quantity:.1f} birim\n"
        response += f"• Toplam değer: {production_summary.total_value:.2f} TL\n"
        response += f"• Hayvan başına ortalama: {production_summary.average_per_animal:.1f} birim\n"
        response += f"• Trend: {self._get_trend_emoji(production_summary.trend)} {production_summary.trend}\n\n"
        
        # Detaylı üretim kayıtları
        production_records = crud.get_production_records(self.db, farm_id, limit=5)
        if production_records:
            response += f"📋 **Son Üretim Kayıtları:**\n"
            for record in production_records:
                response += f"• {record.record_date.strftime('%d.%m.%Y')}: {record.quantity} {record.unit} ({record.production_type})\n"
        
        suggestions = ["Haftalık üretim raporu", "Hayvan başına performans", "Üretim trendi"]
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {
                "total_quantity": production_summary.total_quantity,
                "total_value": production_summary.total_value,
                "trend": production_summary.trend
            }
        }
    
    def _get_health_response(self, farm_id: int, query_analysis: Dict) -> Dict[str, Any]:
        """Sağlık yanıtı üretir"""
        
        health_summary = self.analytics_service.get_health_summary(farm_id)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"🏥 **{farm.name} Sağlık Durumu**\n\n"
        
        response += f"📊 **Sağlık İstatistikleri:**\n"
        response += f"• Toplam aşı sayısı: {health_summary.total_vaccinations}\n"
        response += f"• Bekleyen aşılar: {health_summary.pending_vaccinations}\n"
        response += f"• Geciken aşılar: {health_summary.overdue_vaccinations}\n"
        response += f"• Toplam tedavi: {health_summary.total_treatments}\n"
        response += f"• Aktif sağlık sorunları: {health_summary.active_health_issues}\n\n"
        
        # Yaklaşan aşılar
        upcoming_vaccinations = crud.get_upcoming_vaccinations(self.db, farm_id, 30)
        if upcoming_vaccinations:
            response += f"⚠️ **Yaklaşan Aşılar:**\n"
            for vaccination in upcoming_vaccinations[:3]:  # İlk 3'ü göster
                animal = crud.get_animal(self.db, vaccination.animal_id) if vaccination.animal_id else None
                animal_name = animal.name if animal else "Çiftlik geneli"
                response += f"• {animal_name}: {vaccination.next_due_date.strftime('%d.%m.%Y')}\n"
        
        suggestions = []
        if health_summary.overdue_vaccinations > 0:
            suggestions.append("Geciken aşılar listesi")
        if health_summary.pending_vaccinations > 0:
            suggestions.append("Aşı programı")
        suggestions.extend(["Sağlık kayıtları", "Veteriner randevusu"])
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {
                "total_vaccinations": health_summary.total_vaccinations,
                "pending_vaccinations": health_summary.pending_vaccinations,
                "overdue_vaccinations": health_summary.overdue_vaccinations
            }
        }
    
    def _get_vet_appointments_response(self, farm_id: int) -> Dict[str, Any]:
        """Veteriner randevularını listeler (yaklaşan aşı/tedavi/kontrol tarihleri)."""
        appointments = crud.get_upcoming_health_appointments(self.db, farm_id, days_ahead=90)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"📅 **{farm.name} – Veteriner Randevuları**\n\n"
        
        if not appointments:
            response += "Kayıtlı yaklaşan randevunuz bulunmuyor.\n\n"
            response += "Aşı veya kontrol için **Sağlık kaydı** ekleyerek sonraki tarih (next_due_date) belirtebilirsiniz; bu liste otomatik güncellenir.\n"
            suggestions = ["Sağlık kaydı ekle", "Sağlık durumu", "Yaklaşan aşılar"]
        else:
            response += f"Önümüzdeki 90 gün içinde **{len(appointments)}** randevu kaydı var:\n\n"
            for i, rec in enumerate(appointments[:15], 1):
                animal_name = "Çiftlik geneli"
                if rec.animal_id:
                    animal = crud.get_animal(self.db, rec.animal_id)
                    animal_name = (animal.name or animal.tag_number) if animal else "Bilinmeyen hayvan"
                tarih = rec.next_due_date.strftime("%d.%m.%Y") if rec.next_due_date else "—"
                tip = rec.record_type or "kontrol"
                desc = (rec.description or "")[:50] + ("..." if len(rec.description or "") > 50 else "")
                vet = f" – Dr. {rec.veterinarian}" if rec.veterinarian else ""
                response += f"**{i}. {tarih}** – {animal_name}\n"
                response += f"   {tip}: {desc}{vet}\n\n"
            if len(appointments) > 15:
                response += f"_… ve {len(appointments) - 15} randevu daha._\n\n"
            suggestions = ["Sağlık durumu", "Sağlık kayıtları", "Geciken aşılar"]
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {"appointments_count": len(appointments)}
        }
    
    def _get_financial_response(self, farm_id: int, query_analysis: Dict) -> Dict[str, Any]:
        """Finansal yanıt üretir"""
        
        financial_summary = self.analytics_service.get_financial_summary(farm_id, 30)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"💰 **{farm.name} Finansal Durumu**\n\n"
        
        response += f"📊 **Bu Ayki Finansal Özet:**\n"
        response += f"• Toplam gelir: {financial_summary.total_income:.2f} TL\n"
        response += f"• Toplam gider: {financial_summary.total_expenses:.2f} TL\n"
        response += f"• Net kâr: {financial_summary.net_profit:.2f} TL\n"
        response += f"• Kâr marjı: {financial_summary.profit_margin:.1f}%\n\n"
        
        # Gelir kategorileri
        if financial_summary.income_by_category:
            response += f"📈 **Gelir Kategorileri:**\n"
            for category, amount in financial_summary.income_by_category.items():
                response += f"• {category}: {amount:.2f} TL\n"
        
        # Gider kategorileri
        if financial_summary.expenses_by_category:
            response += f"\n📉 **Gider Kategorileri:**\n"
            for category, amount in financial_summary.expenses_by_category.items():
                response += f"• {category}: {amount:.2f} TL\n"
        
        suggestions = []
        if financial_summary.net_profit < 0:
            suggestions.append("Gider azaltma önerileri")
        suggestions.extend(["Aylık finansal rapor", "Kârlılık analizi", "Maliyet optimizasyonu"])
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {
                "total_income": financial_summary.total_income,
                "total_expenses": financial_summary.total_expenses,
                "net_profit": financial_summary.net_profit,
                "profit_margin": financial_summary.profit_margin
            }
        }
    
    def _get_animal_response(self, farm_id: int, query_analysis: Dict) -> Dict[str, Any]:
        """Hayvan yanıtı üretir"""
        
        animals = crud.get_farm_animals(self.db, farm_id, limit=10)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"🐄 **{farm.name} Hayvan Durumu**\n\n"
        
        # Hayvan sayıları
        species_count = {}
        for animal in animals:
            species_count[animal.species] = species_count.get(animal.species, 0) + 1
        
        response += f"📊 **Hayvan Sayıları:**\n"
        for species, count in species_count.items():
            response += f"• {species}: {count} adet\n"
        
        # Son eklenen hayvanlar
        if animals:
            response += f"\n📋 **Son Eklenen Hayvanlar:**\n"
            for animal in animals[:5]:
                response += f"• {animal.tag_number}: {animal.species}"
                if animal.name:
                    response += f" ({animal.name})"
                response += f" - {animal.status}\n"
        
        suggestions = ["Hayvan detayları", "Hayvan performansı", "Hayvan ekle", "Hayvan güncelle"]
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": {
                "total_animals": len(animals),
                "species_count": species_count
            }
        }
    
    def _get_feed_response(self, farm_id: int, query_analysis: Dict) -> Dict[str, Any]:
        """Yem yanıtı üretir"""
        
        feed_efficiency = self.analytics_service.get_feed_efficiency(farm_id, 30)
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"🌾 **{farm.name} Yem Analizi**\n\n"
        
        response += f"📊 **Son 30 Günlük Yem Verimliliği:**\n"
        response += f"• Toplam yem miktarı: {feed_efficiency['total_feed_quantity']:.1f} kg\n"
        response += f"• Toplam yem maliyeti: {feed_efficiency['total_feed_cost']:.2f} TL\n"
        response += f"• Toplam üretim: {feed_efficiency['total_production']:.1f} birim\n"
        response += f"• Yem verimliliği: {feed_efficiency['feed_efficiency']:.2f} kg yem/kg üretim\n"
        response += f"• Yem maliyeti per üretim: {feed_efficiency['feed_cost_per_production']:.2f} TL/kg\n\n"
        
        # Yem önerileri
        if feed_efficiency['feed_efficiency'] > 3.0:
            response += f"💡 **Öneri:** Yem verimliliğiniz yüksek. Yem kalitesini artırmayı düşünebilirsiniz.\n"
        elif feed_efficiency['feed_efficiency'] < 2.0:
            response += f"💡 **Öneri:** Yem verimliliğiniz düşük. Yem programını gözden geçirmenizi öneririm.\n"
        
        suggestions = ["Yem maliyeti analizi", "Yem programı optimizasyonu", "Yem kayıtları"]
        
        return {
            "response": response,
            "suggestions": suggestions,
            "data": feed_efficiency
        }
    
    def _get_general_response(self, farm_id: int, query: str) -> Dict[str, Any]:
        """Genel yanıt üretir"""
        
        farm = crud.get_farm(self.db, farm_id)
        
        response = f"🤖 **{farm.name} Çiftlik Asistanı**\n\n"
        response += f"Size nasıl yardımcı olabilirim? Aşağıdaki konularda sorular sorabilirsiniz:\n\n"
        response += f"📊 **Çiftlik Durumu:** 'Çiftliğimin genel durumu nasıl?'\n"
        response += f"📈 **Üretim:** 'Bu ayki üretimim nasıl?'\n"
        response += f"🏥 **Sağlık:** 'Hangi hayvanlarımın aşısı yaklaşıyor?'\n"
        response += f"💰 **Finansal:** 'Bu ayki gelir-gider durumum nasıl?'\n"
        response += f"🐄 **Hayvanlar:** 'Hayvanlarımın durumu nasıl?'\n"
        response += f"🌾 **Yem:** 'Yem verimliliğim nasıl?'\n"
        
        suggestions = [
            "Çiftlik durumu",
            "Üretim raporu",
            "Sağlık kontrolü",
            "Finansal analiz",
            "Hayvan listesi",
            "Yem analizi"
        ]
        
        return {
            "response": response,
            "suggestions": suggestions
        }
    
    def _get_trend_emoji(self, trend: str) -> str:
        """Trend için emoji döndürür"""
        if trend == "increasing":
            return "📈"
        elif trend == "decreasing":
            return "📉"
        else:
            return "➡️"
    
    def get_smart_suggestions(self, farm_id: int) -> List[str]:
        """Akıllı öneriler üretir"""
        
        analytics = self.analytics_service.get_farm_dashboard(farm_id)
        suggestions = []
        
        # Kâr durumuna göre öneriler
        if analytics.profit_this_month < 0:
            suggestions.append("Giderleri azaltma stratejileri")
            suggestions.append("Gelir artırma yöntemleri")
        
        # Sağlık durumuna göre öneriler
        if analytics.upcoming_vaccinations > 0:
            suggestions.append("Aşı programı planlama")
        
        if analytics.overdue_health_checks > 0:
            suggestions.append("Geciken sağlık kontrolleri")
        
        # Üretim durumuna göre öneriler
        if analytics.total_production_this_month > 0:
            suggestions.append("Üretim optimizasyonu")
            suggestions.append("Verimlilik artırma")
        
        # Genel öneriler
        suggestions.extend([
            "Yem maliyeti analizi",
            "Hayvan performans değerlendirmesi",
            "Finansal planlama",
            "Çiftlik büyütme stratejileri"
        ])
        
        return suggestions[:6]  # İlk 6 öneriyi döndür


