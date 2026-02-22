#!/usr/bin/env python3
"""
Test authenticated access to farm data
"""

import requests
import json

print("🔐 Testing Authenticated Access")
print("=" * 40)

# Login first
login_data = {
    "email": "admin@livestock.com",
    "password": "admin123"
}

response = requests.post("http://localhost:8000/auth/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("✅ Login successful")
    
    # Test 1: Access smart-farm with token
    print("\n1. Testing /smart-farm with authentication...")
    response = requests.get("http://localhost:8000/smart-farm", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ PASS: Smart farm page accessible with authentication")
    else:
        print("   ❌ FAIL: Smart farm page not accessible with authentication")
    
    # Test 2: Access farm list with token
    print("\n2. Testing /farm/ with authentication...")
    response = requests.get("http://localhost:8000/farm/", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        farms = response.json()
        print(f"   ✅ PASS: Farm list accessible - {len(farms)} farms found")
    else:
        print("   ❌ FAIL: Farm list not accessible with authentication")
    
    # Test 3: Access specific farm with token
    print("\n3. Testing /farm/1 with authentication...")
    response = requests.get("http://localhost:8000/farm/1", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        farm = response.json()
        print(f"   ✅ PASS: Specific farm accessible - {farm['name']}")
    else:
        print("   ❌ FAIL: Specific farm not accessible with authentication")
    
    # Test 4: Access farm analytics with token
    print("\n4. Testing /farm/1/analytics/summary with authentication...")
    response = requests.get("http://localhost:8000/farm/1/analytics/summary", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        analytics = response.json()
        print(f"   ✅ PASS: Farm analytics accessible - {analytics.get('total_animals', 0)} animals")
    else:
        print("   ❌ FAIL: Farm analytics not accessible with authentication")
    
    # Test 5: Access farm animals with token
    print("\n5. Testing /farm/1/animals with authentication...")
    response = requests.get("http://localhost:8000/farm/1/animals", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        animals = response.json()
        print(f"   ✅ PASS: Farm animals accessible - {len(animals)} animals")
    else:
        print("   ❌ FAIL: Farm animals not accessible with authentication")
    
    # Test 6: Access farm chat with token
    print("\n6. Testing /farm/1/chat with authentication...")
    response = requests.post("http://localhost:8000/farm/1/chat", 
                           json={"message": "Çiftliğimin durumu nasıl?"}, 
                           headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        chat_response = response.json()
        print(f"   ✅ PASS: Farm chat accessible - Response received")
    else:
        print("   ❌ FAIL: Farm chat not accessible with authentication")
    
else:
    print("❌ Login failed")

print("\n" + "=" * 40)
print("🔐 Authenticated Access Test Completed")


