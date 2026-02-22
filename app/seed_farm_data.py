from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
from app.database import SessionLocal
from app import models, crud, schemas

def create_sample_farm_data():
    """Örnek çiftlik verileri oluştur"""
    db = SessionLocal()
    
    try:
        # Örnek kullanıcı oluştur (eğer yoksa)
        user = crud.get_user_by_email(db, "ciftci@example.com")
        if not user:
            user_data = schemas.UserCreate(
                email="ciftci@example.com",
                username="ciftci",
                password="password123",
                full_name="Örnek Çiftçi"
            )
            user = crud.create_user(db, user_data)
            print(f"Örnek kullanıcı oluşturuldu: {user.email}")
        
        # Örnek çiftlik oluştur
        farm_data = schemas.FarmCreate(
            name="Örnek Sığır Çiftliği",
            location="Ankara, Türkiye",
            farm_type="cattle",
            total_area=50.0,
            established_date=datetime(2020, 1, 1)
        )
        farm = crud.create_farm(db, farm_data, user.id)
        print(f"Örnek çiftlik oluşturuldu: {farm.name}")
        
        # Örnek hayvanlar oluştur
        animals_data = [
            {"tag_number": "TR001", "name": "Bella", "species": "cattle", "breed": "Holstein", "gender": "female", "birth_date": datetime(2019, 3, 15), "weight": 450.0, "purchase_price": 15000.0},
            {"tag_number": "TR002", "name": "Max", "species": "cattle", "breed": "Holstein", "gender": "male", "birth_date": datetime(2018, 7, 22), "weight": 600.0, "purchase_price": 20000.0},
            {"tag_number": "TR003", "name": "Luna", "species": "cattle", "breed": "Holstein", "gender": "female", "birth_date": datetime(2020, 1, 10), "weight": 400.0, "purchase_price": 12000.0},
            {"tag_number": "TR004", "name": "Charlie", "species": "cattle", "breed": "Holstein", "gender": "male", "birth_date": datetime(2019, 11, 5), "weight": 550.0, "purchase_price": 18000.0},
            {"tag_number": "TR005", "name": "Daisy", "species": "cattle", "breed": "Holstein", "gender": "female", "birth_date": datetime(2021, 2, 18), "weight": 350.0, "purchase_price": 10000.0},
        ]
        
        for animal_data in animals_data:
            animal_data["farm_id"] = farm.id
            animal = crud.create_animal(db, schemas.AnimalCreate(**animal_data))
            print(f"Hayvan oluşturuldu: {animal.tag_number} - {animal.name}")
        
        # Örnek üretim kayıtları oluştur
        animals = crud.get_farm_animals(db, farm.id)
        for i in range(30):  # Son 30 gün için
            date = datetime.now() - timedelta(days=i)
            for animal in animals:
                if animal.gender == "female":  # Sadece dişi hayvanlar süt verir
                    production_data = schemas.ProductionRecordCreate(
                        farm_id=farm.id,
                        animal_id=animal.id,
                        record_date=date,
                        production_type="milk",
                        quantity=random.uniform(15, 35),  # 15-35 litre arası
                        unit="litre",
                        quality_grade=random.choice(["A", "B", "A"]),
                        price_per_unit=random.uniform(8, 12),  # 8-12 TL/litre
                        total_value=0,  # Hesaplanacak
                        notes=f"Günlük süt üretimi - {animal.name}"
                    )
                    production_data.total_value = production_data.quantity * production_data.price_per_unit
                    crud.create_production_record(db, production_data)
        
        print("Üretim kayıtları oluşturuldu")
        
        # Örnek sağlık kayıtları oluştur
        health_records_data = [
            {
                "farm_id": farm.id,
                "animal_id": animals[0].id,
                "record_date": datetime.now() - timedelta(days=10),
                "record_type": "vaccination",
                "description": "Şap aşısı",
                "veterinarian": "Dr. Ahmet Yılmaz",
                "medication": "Şap Aşısı",
                "dosage": "5ml",
                "cost": 150.0,
                "next_due_date": datetime.now() + timedelta(days=20),
                "status": "pending",
                "notes": "Yıllık şap aşısı"
            },
            {
                "farm_id": farm.id,
                "animal_id": animals[1].id,
                "record_date": datetime.now() - timedelta(days=5),
                "record_type": "treatment",
                "description": "Mastitis tedavisi",
                "veterinarian": "Dr. Ayşe Demir",
                "medication": "Antibiyotik",
                "dosage": "10ml x 3 gün",
                "cost": 300.0,
                "status": "completed",
                "notes": "Hafif mastitis, tedavi tamamlandı"
            },
            {
                "farm_id": farm.id,
                "animal_id": animals[2].id,
                "record_date": datetime.now() - timedelta(days=15),
                "record_type": "vaccination",
                "description": "Brucella aşısı",
                "veterinarian": "Dr. Mehmet Kaya",
                "medication": "Brucella Aşısı",
                "dosage": "2ml",
                "cost": 200.0,
                "next_due_date": datetime.now() + timedelta(days=5),
                "status": "pending",
                "notes": "Yıllık brucella aşısı"
            }
        ]
        
        for health_data in health_records_data:
            crud.create_health_record(db, schemas.HealthRecordCreate(**health_data))
        
        print("Sağlık kayıtları oluşturuldu")
        
        # Örnek finansal kayıtlar oluştur
        financial_records_data = [
            # Gelirler
            {
                "farm_id": farm.id,
                "record_date": datetime.now() - timedelta(days=1),
                "record_type": "income",
                "category": "sales",
                "description": "Süt satışı",
                "amount": 2500.0,
                "payment_method": "bank_transfer",
                "notes": "Günlük süt satışı"
            },
            {
                "farm_id": farm.id,
                "record_date": datetime.now() - timedelta(days=2),
                "record_type": "income",
                "category": "sales",
                "description": "Süt satışı",
                "amount": 2300.0,
                "payment_method": "bank_transfer",
                "notes": "Günlük süt satışı"
            },
            # Giderler
            {
                "farm_id": farm.id,
                "record_date": datetime.now() - timedelta(days=3),
                "record_type": "expense",
                "category": "feed",
                "description": "Yem alımı",
                "amount": 800.0,
                "payment_method": "cash",
                "notes": "Aylık yem alımı"
            },
            {
                "farm_id": farm.id,
                "record_date": datetime.now() - timedelta(days=5),
                "record_type": "expense",
                "category": "veterinary",
                "description": "Veteriner hizmeti",
                "amount": 300.0,
                "payment_method": "cash",
                "notes": "Mastitis tedavisi"
            },
            {
                "farm_id": farm.id,
                "record_date": datetime.now() - timedelta(days=7),
                "record_type": "expense",
                "category": "equipment",
                "description": "Süt sağma makinesi bakımı",
                "amount": 500.0,
                "payment_method": "bank_transfer",
                "notes": "Aylık bakım"
            }
        ]
        
        for financial_data in financial_records_data:
            crud.create_financial_record(db, schemas.FinancialRecordCreate(**financial_data))
        
        print("Finansal kayıtlar oluşturuldu")
        
        # Örnek yem kayıtları oluştur
        feed_records_data = [
            {
                "farm_id": farm.id,
                "feed_date": datetime.now() - timedelta(days=1),
                "feed_type": "hay",
                "quantity": 100.0,
                "unit_cost": 2.5,
                "total_cost": 250.0,
                "supplier": "Yem A.Ş.",
                "quality_notes": "Kaliteli yonca samanı"
            },
            {
                "farm_id": farm.id,
                "feed_date": datetime.now() - timedelta(days=2),
                "feed_type": "grain",
                "quantity": 50.0,
                "unit_cost": 4.0,
                "total_cost": 200.0,
                "supplier": "Yem A.Ş.",
                "quality_notes": "Arpa ve mısır karışımı"
            },
            {
                "farm_id": farm.id,
                "feed_date": datetime.now() - timedelta(days=3),
                "feed_type": "supplement",
                "quantity": 20.0,
                "unit_cost": 8.0,
                "total_cost": 160.0,
                "supplier": "Beslenme Ltd.",
                "quality_notes": "Vitamin ve mineral takviyesi"
            }
        ]
        
        for feed_data in feed_records_data:
            crud.create_feed_record(db, schemas.FeedRecordCreate(**feed_data))
        
        print("Yem kayıtları oluşturuldu")
        
        print("\n✅ Örnek çiftlik verileri başarıyla oluşturuldu!")
        print(f"📧 Kullanıcı: ciftci@example.com")
        print(f"🔑 Şifre: password123")
        print(f"🏡 Çiftlik: {farm.name}")
        print(f"🐄 Hayvan sayısı: {len(animals)}")
        
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_farm_data()


