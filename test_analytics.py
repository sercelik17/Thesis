#!/usr/bin/env python3
"""
Test farm analytics
"""

import requests
import json

# Login
login_data = {
    "email": "admin@livestock.com",
    "password": "admin123"
}

response = requests.post("http://localhost:8000/auth/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    farm_id = 1
    
    print("Testing farm analytics...")
    
    # Test farm summary
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/analytics/summary", headers=headers)
    if response.status_code == 200:
        analytics = response.json()
        print("📊 Farm Analytics Summary:")
        print(f"  - Total Animals: {analytics.get('total_animals', 0)}")
        print(f"  - Monthly Production: {analytics.get('total_production_this_month', 0):.2f} kg/lt")
        print(f"  - Monthly Income: {analytics.get('total_income_this_month', 0):.2f} TL")
        print(f"  - Monthly Expenses: {analytics.get('total_expenses_this_month', 0):.2f} TL")
        print(f"  - Monthly Profit: {analytics.get('profit_this_month', 0):.2f} TL")
        print(f"  - Upcoming Vaccinations: {analytics.get('upcoming_vaccinations', 0)}")
        print(f"  - Overdue Health Checks: {analytics.get('overdue_health_checks', 0)}")
        print(f"  - Avg Daily Milk Production: {analytics.get('average_daily_milk_production', 0):.2f} lt")
        print(f"  - Feed Cost per Animal: {analytics.get('feed_cost_per_animal', 0):.2f} TL")
    else:
        print(f"Analytics error: {response.text}")
    
    print("\nTesting production records...")
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/production-records", headers=headers)
    if response.status_code == 200:
        records = response.json()
        print(f"  - Total production records: {len(records)}")
        if records:
            print(f"  - Latest record: {records[0]['production_type']} - {records[0]['quantity']} {records[0]['unit']}")
    else:
        print(f"Production records error: {response.text}")
    
    print("\nTesting financial records...")
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/financial-records", headers=headers)
    if response.status_code == 200:
        records = response.json()
        print(f"  - Total financial records: {len(records)}")
        if records:
            print(f"  - Latest record: {records[0]['record_type']} - {records[0]['description']} - {records[0]['amount']} TL")
    else:
        print(f"Financial records error: {response.text}")
    
    print("\nTesting health records...")
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/health-records", headers=headers)
    if response.status_code == 200:
        records = response.json()
        print(f"  - Total health records: {len(records)}")
        if records:
            print(f"  - Latest record: {records[0]['record_type']} - {records[0]['description']}")
    else:
        print(f"Health records error: {response.text}")
    
    print("\nTesting feed records...")
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/feed-records", headers=headers)
    if response.status_code == 200:
        records = response.json()
        print(f"  - Total feed records: {len(records)}")
        if records:
            print(f"  - Latest record: {records[0]['feed_type']} - {records[0]['quantity']} kg")
    else:
        print(f"Feed records error: {response.text}")
    
    print("\nTesting animals...")
    response = requests.get(f"http://localhost:8000/farm/{farm_id}/animals", headers=headers)
    if response.status_code == 200:
        animals = response.json()
        print(f"  - Total animals: {len(animals)}")
        for animal in animals:
            print(f"    - {animal['tag_number']}: {animal['name']} ({animal['species']}, {animal['breed']})")
    else:
        print(f"Animals error: {response.text}")
    
    print("\n✅ Analytics test completed!")
    
else:
    print(f"Login failed: {response.text}")


