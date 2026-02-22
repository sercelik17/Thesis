#!/usr/bin/env python3
"""
Add sample farm data for analysis
"""

import requests
import json
from datetime import datetime, timedelta

# Login
login_data = {
    "email": "admin@livestock.com",
    "password": "admin123"
}

response = requests.post("http://localhost:8000/auth/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    farm_id = 1  # Test çiftliği ID'si
    
    print("Adding animals...")
    # Add animals
    animals = [
        {
            "farm_id": farm_id,
            "tag_number": "001",
            "name": "Bella",
            "species": "cattle",
            "breed": "Holstein",
            "gender": "female",
            "birth_date": "2020-03-15T00:00:00",
            "weight": 450.0,
            "status": "active",
            "purchase_price": 15000.0,
            "notes": "Ana süt ineği"
        },
        {
            "farm_id": farm_id,
            "tag_number": "002", 
            "name": "Max",
            "species": "cattle",
            "breed": "Holstein",
            "gender": "male",
            "birth_date": "2019-08-20T00:00:00",
            "weight": 650.0,
            "status": "active",
            "purchase_price": 20000.0,
            "notes": "Boğa"
        },
        {
            "farm_id": farm_id,
            "tag_number": "003",
            "name": "Luna",
            "species": "cattle", 
            "breed": "Holstein",
            "gender": "female",
            "birth_date": "2021-01-10T00:00:00",
            "weight": 380.0,
            "status": "active",
            "purchase_price": 12000.0,
            "notes": "Genç inek"
        }
    ]
    
    for animal in animals:
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/animals/", json=animal, headers=headers)
        if response.status_code == 200:
            print(f"Animal {animal['tag_number']} added successfully")
        else:
            print(f"Error adding animal {animal['tag_number']}: {response.text}")
    
    print("\nAdding production records...")
    # Add production records (last 30 days)
    today = datetime.now()
    for i in range(30):
        date = today - timedelta(days=i)
        production_data = {
            "farm_id": farm_id,
            "animal_id": 1,  # Bella
            "record_date": date.isoformat(),
            "production_type": "milk",
            "quantity": 25.0 + (i % 5),  # 25-29 litre arası
            "unit": "litre",
            "quality_grade": "A",
            "price_per_unit": 8.5,
            "total_value": (25.0 + (i % 5)) * 8.5,
            "notes": f"Günlük süt üretimi - {date.strftime('%Y-%m-%d')}"
        }
        
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/production-records/", json=production_data, headers=headers)
        if response.status_code == 200:
            print(f"Production record for {date.strftime('%Y-%m-%d')} added")
        else:
            print(f"Error adding production record: {response.text}")
    
    print("\nAdding financial records...")
    # Add financial records
    financial_records = [
        {
            "farm_id": farm_id,
            "record_date": (today - timedelta(days=1)).isoformat(),
            "record_type": "income",
            "category": "sales",
            "description": "Süt satışı",
            "amount": 2500.0,
            "payment_method": "bank_transfer",
            "notes": "Günlük süt satışı"
        },
        {
            "farm_id": farm_id,
            "record_date": (today - timedelta(days=2)).isoformat(),
            "record_type": "expense",
            "category": "feed",
            "description": "Yem alımı",
            "amount": 800.0,
            "payment_method": "cash",
            "notes": "Günlük yem maliyeti"
        },
        {
            "farm_id": farm_id,
            "record_date": (today - timedelta(days=3)).isoformat(),
            "record_type": "expense",
            "category": "veterinary",
            "description": "Veteriner kontrolü",
            "amount": 300.0,
            "payment_method": "bank_transfer",
            "notes": "Rutin sağlık kontrolü"
        }
    ]
    
    for record in financial_records:
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/financial-records/", json=record, headers=headers)
        if response.status_code == 200:
            print(f"Financial record added: {record['description']}")
        else:
            print(f"Error adding financial record: {response.text}")
    
    print("\nAdding health records...")
    # Add health records
    health_records = [
        {
            "farm_id": farm_id,
            "animal_id": 1,
            "record_date": (today - timedelta(days=5)).isoformat(),
            "record_type": "vaccination",
            "description": "Aşı uygulaması",
            "veterinarian": "Dr. Ahmet Yılmaz",
            "medication": "Brucella aşısı",
            "cost": 150.0,
            "next_due_date": (today + timedelta(days=365)).isoformat(),
            "status": "completed",
            "notes": "Yıllık aşı programı"
        },
        {
            "farm_id": farm_id,
            "animal_id": 2,
            "record_date": (today - timedelta(days=10)).isoformat(),
            "record_type": "checkup",
            "description": "Genel sağlık kontrolü",
            "veterinarian": "Dr. Ahmet Yılmaz",
            "cost": 200.0,
            "status": "completed",
            "notes": "Rutin kontrol"
        }
    ]
    
    for record in health_records:
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/health-records/", json=record, headers=headers)
        if response.status_code == 200:
            print(f"Health record added: {record['description']}")
        else:
            print(f"Error adding health record: {response.text}")
    
    print("\nAdding feed records...")
    # Add feed records
    feed_records = [
        {
            "farm_id": farm_id,
            "animal_id": 1,
            "feed_date": (today - timedelta(days=1)).isoformat(),
            "feed_type": "grain",
            "quantity": 15.0,
            "unit_cost": 2.5,
            "total_cost": 37.5,
            "supplier": "Yem A.Ş.",
            "quality_notes": "Kaliteli yem"
        },
        {
            "farm_id": farm_id,
            "animal_id": 2,
            "feed_date": (today - timedelta(days=1)).isoformat(),
            "feed_type": "hay",
            "quantity": 20.0,
            "unit_cost": 1.8,
            "total_cost": 36.0,
            "supplier": "Yem A.Ş.",
            "quality_notes": "Taze ot"
        }
    ]
    
    for record in feed_records:
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/feed-records/", json=record, headers=headers)
        if response.status_code == 200:
            print(f"Feed record added: {record['feed_type']}")
        else:
            print(f"Error adding feed record: {response.text}")
    
    print("\n✅ Sample data added successfully!")
    print("Now you can test the analytics and chat features!")
    
else:
    print(f"Login failed: {response.text}")


