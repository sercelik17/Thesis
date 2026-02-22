#!/usr/bin/env python3
"""
Test smart farm page access
"""

import requests
import json

print("🧪 Testing Smart Farm Page Access")
print("=" * 40)

# Test 1: Access smart-farm page without authentication (should work now)
print("\n1. Testing /smart-farm page access without authentication...")
try:
    response = requests.get("http://localhost:8000/smart-farm")
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ PASS: Smart farm page accessible (HTML served)")
        print(f"   Content length: {len(response.text)} characters")
    else:
        print("   ❌ FAIL: Smart farm page not accessible")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 2: Login and get token
print("\n2. Testing login to get token...")
login_data = {
    "email": "admin@livestock.com",
    "password": "admin123"
}

response = requests.post("http://localhost:8000/auth/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"   ✅ PASS: Login successful, token received")
    print(f"   Token length: {len(token)} characters")
    
    # Test 3: Access farm data with token
    print("\n3. Testing farm data access with token...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://localhost:8000/farm/", headers=headers)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        farms = response.json()
        print(f"   ✅ PASS: Farm data accessible - {len(farms)} farms found")
    else:
        print("   ❌ FAIL: Farm data not accessible with token")
        print(f"   Response: {response.text[:200]}...")
        
else:
    print(f"   ❌ FAIL: Login failed - {response.text}")

print("\n" + "=" * 40)
print("🧪 Smart Farm Access Test Completed")


