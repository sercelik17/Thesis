#!/usr/bin/env python3
"""
Akıllı Çiftlik Yönetim Sistemi Test Uygulaması
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

# Basit test uygulaması
app = FastAPI(
    title="Akıllı Çiftlik Yönetim Sistemi",
    description="Yapay zeka destekli çiftlik yönetimi ve analiz platformu",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Ana sayfa"""
    return {
        "message": "🏡 Akıllı Çiftlik Yönetim Sistemi",
        "version": "2.0.0",
        "features": [
            "Çiftlik veri yönetimi",
            "Hayvan takibi",
            "Üretim analizi",
            "Sağlık kontrolü",
            "Finansal raporlama",
            "Yapay zeka destekli sohbet"
        ],
        "endpoints": {
            "smart_farm": "/smart-farm",
            "docs": "/docs"
        }
    }

@app.get("/smart-farm", response_class=HTMLResponse)
async def smart_farm_interface():
    """Akıllı çiftlik arayüzü"""
    try:
        with open("static/smart_farm.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Akıllı Çiftlik Yönetim Sistemi</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    margin: 0;
                    padding: 20px;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .container {
                    background: white;
                    border-radius: 20px;
                    padding: 40px;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                    text-align: center;
                    max-width: 600px;
                }
                h1 {
                    color: #667eea;
                    margin-bottom: 20px;
                    font-size: 2.5rem;
                }
                p {
                    color: #666;
                    font-size: 1.2rem;
                    line-height: 1.6;
                    margin-bottom: 30px;
                }
                .features {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }
                .feature {
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 10px;
                    border-left: 4px solid #667eea;
                }
                .feature h3 {
                    color: #667eea;
                    margin-bottom: 10px;
                }
                .demo-button {
                    background: #667eea;
                    color: white;
                    padding: 15px 30px;
                    border: none;
                    border-radius: 25px;
                    font-size: 1.1rem;
                    cursor: pointer;
                    text-decoration: none;
                    display: inline-block;
                    margin: 10px;
                    transition: background 0.3s ease;
                }
                .demo-button:hover {
                    background: #5a6fd8;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏡 Akıllı Çiftlik Yönetim Sistemi</h1>
                <p>Yapay zeka destekli çiftlik yönetimi ve analiz platformu</p>
                
                <div class="features">
                    <div class="feature">
                        <h3>📊 Veri Yönetimi</h3>
                        <p>Çiftlik, hayvan, üretim ve sağlık verilerini yönetin</p>
                    </div>
                    <div class="feature">
                        <h3>🤖 AI Asistan</h3>
                        <p>Yapay zeka destekli sohbet ile çiftliğinizi analiz edin</p>
                    </div>
                    <div class="feature">
                        <h3>📈 Analiz</h3>
                        <p>Üretim, finansal ve sağlık analizleri</p>
                    </div>
                    <div class="feature">
                        <h3>📱 Modern Arayüz</h3>
                        <p>Responsive ve kullanıcı dostu tasarım</p>
                    </div>
                </div>
                
                <h2>🚀 Sistem Özellikleri</h2>
                <ul style="text-align: left; color: #666; line-height: 1.8;">
                    <li><strong>Çiftlik Yönetimi:</strong> Çiftlik bilgileri, hayvan kayıtları, üretim takibi</li>
                    <li><strong>Sağlık Kontrolü:</strong> Aşı takibi, hastalık kayıtları, veteriner randevuları</li>
                    <li><strong>Finansal Analiz:</strong> Gelir-gider takibi, kârlılık analizi, maliyet optimizasyonu</li>
                    <li><strong>Üretim Analizi:</strong> Süt, et, yumurta üretim takibi ve verimlilik analizi</li>
                    <li><strong>Yem Yönetimi:</strong> Yem tüketimi, maliyet analizi, verimlilik hesaplamaları</li>
                    <li><strong>Akıllı Öneriler:</strong> AI destekli çiftlik yönetimi önerileri</li>
                </ul>
                
                <h2>💡 Örnek Sorgular</h2>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <p style="color: #666; font-style: italic;">
                        "Çiftliğimin genel durumu nasıl?"<br>
                        "Bu ayki üretimim geçen aya göre nasıl?"<br>
                        "Hangi hayvanlarımın aşısı yaklaşıyor?"<br>
                        "Yem maliyetlerim ortalamadan yüksek mi?"<br>
                        "En kârlı hayvanlarım hangileri?"
                    </p>
                </div>
                
                <a href="/docs" class="demo-button">📚 API Dokümantasyonu</a>
                <a href="/" class="demo-button">🏠 Ana Sayfa</a>
            </div>
        </body>
        </html>
        """)

@app.get("/health")
async def health_check():
    """Sistem durumu kontrolü"""
    return {
        "status": "healthy",
        "system": "Akıllı Çiftlik Yönetim Sistemi",
        "version": "2.0.0",
        "features": {
            "farm_management": "✅ Aktif",
            "animal_tracking": "✅ Aktif", 
            "production_analysis": "✅ Aktif",
            "health_monitoring": "✅ Aktif",
            "financial_reporting": "✅ Aktif",
            "ai_chat": "✅ Aktif"
        }
    }

if __name__ == "__main__":
    print("=" * 60)
    print("🏡 Akıllı Çiftlik Yönetim Sistemi")
    print("=" * 60)
    print("🚀 Sistem başlatılıyor...")
    print("📱 Akıllı Çiftlik Arayüzü: http://localhost:8000/smart-farm")
    print("📚 API Dokümantasyonu: http://localhost:8000/docs")
    print("🏠 Ana Sayfa: http://localhost:8000")
    print("=" * 60)
    
    uvicorn.run(
        "test_smart_farm:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


