#!/usr/bin/env python3
"""
Hayvancılık AI Sohbet Robotu - Ana Çalıştırma Dosyası
Bu dosya uygulamayı başlatmak için kullanılır.
"""

import uvicorn
from app.main import app
from app.config import settings
from app.database import engine
from app import models
from app.seed_data import seed_livestock_knowledge, seed_rag_system
from sqlalchemy.orm import Session

def initialize_database():
    """Veritabanını başlat ve örnek verileri yükle"""
    print("Veritabanı tabloları oluşturuluyor...")
    models.Base.metadata.create_all(bind=engine)
    
    print("Örnek veriler yükleniyor...")
    db = Session(engine)
    try:
        seed_livestock_knowledge(db)
        print("Hayvancılık bilgi veritabanı hazırlandı.")
    except Exception as e:
        print(f"Veritabanı başlatma hatası: {e}")
    finally:
        db.close()

def initialize_rag_system():
    """RAG sistemini başlat"""
    print("RAG sistemi başlatılıyor...")
    try:
        seed_rag_system()
        print("RAG sistemi hazır.")
    except Exception as e:
        print(f"RAG sistemi başlatma hatası: {e}")

def main():
    """Ana fonksiyon"""
    print("=" * 60)
    print("🐄 Hayvancılık AI Sohbet Robotu")
    print("=" * 60)
    print(f"Uygulama: {settings.APP_NAME}")
    print(f"Debug Modu: {settings.DEBUG}")
    print(f"Host: {settings.HOST}")
    print(f"Port: {settings.PORT}")
    print("=" * 60)
    
    # Veritabanını başlat
    initialize_database()
    
    # RAG sistemini başlat
    initialize_rag_system()
    
    print("\n🚀 Uygulama başlatılıyor...")
    print(f"📱 Kullanıcı Arayüzü: http://{settings.HOST}:{settings.PORT}/chat")
    print(f"🔧 Admin Paneli: http://{settings.HOST}:{settings.PORT}/admin")
    print(f"📚 API Dokümantasyonu: http://{settings.HOST}:{settings.PORT}/docs")
    print("\nÇıkmak için Ctrl+C tuşlarına basın.")
    print("=" * 60)
    
    # Uygulamayı başlat
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )

if __name__ == "__main__":
    main()

