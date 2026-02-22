#!/usr/bin/env python3
"""
Test farm creation
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
    print(f"Login successful, token: {token[:50]}...")
    
    # Create farm
    headers = {"Authorization": f"Bearer {token}"}
    farm_data = {
        "name": "Test Çiftliği",
        "location": "Ankara, Türkiye",
        "farm_type": "cattle",
        "total_area": 100.0
    }
    
    response = requests.post("http://localhost:8000/farm/", json=farm_data, headers=headers)
    print(f"Farm creation status: {response.status_code}")
    if response.status_code == 200:
        farm = response.json()
        print(f"Farm created: {farm}")
    else:
        print(f"Error: {response.text}")
        
    # List farms
    response = requests.get("http://localhost:8000/farm/", headers=headers)
    print(f"Farm list status: {response.status_code}")
    if response.status_code == 200:
        farms = response.json()
        print(f"Farms: {farms}")
    else:
        print(f"Error: {response.text}")
        
else:
    print(f"Login failed: {response.text}")


