#!/usr/bin/env python3
"""
Test security - try to access farm data without authentication
"""

import requests
import json

print("🔒 Testing Security - Unauthorized Access Prevention")
print("=" * 50)

# Test 1: Try to access smart-farm without token
print("\n1. Testing /smart-farm without authentication...")
try:
    response = requests.get("http://localhost:8000/smart-farm")
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Smart farm page requires authentication")
    else:
        print("   ❌ FAIL: Smart farm page accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 2: Try to access farm list without token
print("\n2. Testing /farm/ without authentication...")
try:
    response = requests.get("http://localhost:8000/farm/")
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Farm list requires authentication")
    else:
        print("   ❌ FAIL: Farm list accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 3: Try to access specific farm without token
print("\n3. Testing /farm/1 without authentication...")
try:
    response = requests.get("http://localhost:8000/farm/1")
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Specific farm requires authentication")
    else:
        print("   ❌ FAIL: Specific farm accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 4: Try to access farm analytics without token
print("\n4. Testing /farm/1/analytics/summary without authentication...")
try:
    response = requests.get("http://localhost:8000/farm/1/analytics/summary")
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Farm analytics requires authentication")
    else:
        print("   ❌ FAIL: Farm analytics accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 5: Try to access farm animals without token
print("\n5. Testing /farm/1/animals without authentication...")
try:
    response = requests.get("http://localhost:8000/farm/1/animals")
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Farm animals requires authentication")
    else:
        print("   ❌ FAIL: Farm animals accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 6: Try to access farm chat without token
print("\n6. Testing /farm/1/chat without authentication...")
try:
    response = requests.post("http://localhost:8000/farm/1/chat", json={"message": "test"})
    print(f"   Status Code: {response.status_code}")
    if response.status_code in [401, 403]:
        print("   ✅ PASS: Farm chat requires authentication")
    else:
        print("   ❌ FAIL: Farm chat accessible without authentication")
        print(f"   Response: {response.text[:200]}...")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

print("\n" + "=" * 50)
print("🔒 Security Test Completed")
