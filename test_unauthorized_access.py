#!/usr/bin/env python3
"""
Test unauthorized access to smart farm page
"""

import requests
import json

print("🔒 Testing Unauthorized Access Prevention")
print("=" * 50)

# Test 1: Access smart-farm page without token (should show login message)
print("\n1. Testing /smart-farm page access without authentication...")
try:
    response = requests.get("http://localhost:8000/smart-farm")
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        content = response.text
        if "Erişim Gerekli" in content and "Giriş Yap" in content:
            print("   ✅ PASS: Smart farm page shows login message for unauthorized users")
        else:
            print("   ❌ FAIL: Smart farm page doesn't show proper login message")
            print(f"   Content preview: {content[:200]}...")
    else:
        print("   ❌ FAIL: Smart farm page not accessible")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 2: Login and access with valid token
print("\n2. Testing login and access with valid token...")
login_data = {
    "email": "admin@livestock.com",
    "password": "admin123"
}

response = requests.post("http://localhost:8000/auth/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"   ✅ PASS: Login successful, token received")
    
    # Test smart farm page with token
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://localhost:8000/smart-farm", headers=headers)
    print(f"   Smart farm page status: {response.status_code}")
    if response.status_code == 200:
        content = response.text
        if "Akıllı Çiftlik Yönetim Sistemi" in content and "Çiftlik Seçin" in content:
            print("   ✅ PASS: Smart farm page shows full interface for authenticated users")
        else:
            print("   ❌ FAIL: Smart farm page doesn't show proper interface")
    else:
        print("   ❌ FAIL: Smart farm page not accessible with valid token")
        
else:
    print(f"   ❌ FAIL: Login failed - {response.text}")

# Test 3: Test with invalid token
print("\n3. Testing with invalid token...")
invalid_headers = {"Authorization": "Bearer invalid_token_12345"}
response = requests.get("http://localhost:8000/smart-farm", headers=invalid_headers)
print(f"   Status Code: {response.status_code}")
if response.status_code == 200:
    content = response.text
    if "Erişim Gerekli" in content and "Giriş Yap" in content:
        print("   ✅ PASS: Smart farm page shows login message for invalid token")
    else:
        print("   ❌ FAIL: Smart farm page doesn't handle invalid token properly")
else:
    print("   ❌ FAIL: Smart farm page not accessible with invalid token")

print("\n" + "=" * 50)
print("🔒 Unauthorized Access Test Completed")


