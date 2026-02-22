#!/usr/bin/env python3
"""
Test farm chat functionality
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
    
    print("Testing farm chat...")
    
    # Test chat queries
    test_queries = [
        "Çiftliğimin genel durumu nasıl?",
        "Bu ayki üretimim nasıl?",
        "Hangi hayvanlarımın aşısı yaklaşıyor?",
        "Yem maliyetlerim nasıl?",
        "En karlı hayvanlarım hangileri?"
    ]
    
    for query in test_queries:
        print(f"\n🤖 Query: {query}")
        
        chat_data = {
            "message": query,
            "conversation_id": None
        }
        
        response = requests.post(f"http://localhost:8000/farm/{farm_id}/chat", json=chat_data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Response: {result.get('response', 'No response')}")
            print(f"   Conversation ID: {result.get('conversation_id')}")
            print(f"   Message ID: {result.get('message_id')}")
        else:
            print(f"❌ Error: {response.text}")
    
    print("\n✅ Chat test completed!")
    
else:
    print(f"Login failed: {response.text}")
