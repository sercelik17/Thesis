"""
Hayvancılık bilgi veritabanı için örnek veriler
Bu dosya, sistem başlatıldığında hayvancılık konularında temel bilgileri yükler.
"""

LIVESTOCK_KNOWLEDGE_DATA = [
    # Sığır Yetiştiriciliği
    {
        "category": "sığır",
        "subcategory": "beslenme",
        "title": "Sığır Beslenme Temelleri",
        "content": """
        Sığır beslenmesinde dikkat edilmesi gereken temel konular:
        
        1. Kaba Yem: Ot, saman, silaj gibi kaba yemler sığırların temel besin kaynağıdır.
        2. Kesif Yem: Arpa, mısır, soya gibi yüksek enerjili yemler.
        3. Su: Günde 50-100 litre temiz su sağlanmalıdır.
        4. Mineral ve Vitamin: Tuz, kalsiyum, fosfor gibi mineraller önemlidir.
        5. Beslenme Programı: Yaş, cinsiyet ve üretim durumuna göre ayarlanmalıdır.
        
        Beslenme programı veteriner hekim kontrolünde hazırlanmalıdır.
        """,
        "source": "Tarım ve Orman Bakanlığı - Hayvancılık Rehberi"
    },
    {
        "category": "sığır",
        "subcategory": "sağlık",
        "title": "Sığır Hastalıkları ve Korunma",
        "content": """
        Sığırlarda sık görülen hastalıklar ve korunma yöntemleri:
        
        1. Mastitis: Meme iltihabı, hijyen ve düzenli kontrol ile önlenebilir.
        2. Ayak Hastalıkları: Temiz ve kuru zemin, düzenli tırnak bakımı.
        3. Solunum Yolu Hastalıkları: İyi havalandırma, aşılama programı.
        4. Sindirim Sistemi: Dengeli beslenme, ani yem değişikliklerinden kaçınma.
        5. Üreme Hastalıkları: Düzenli veteriner kontrolü, temizlik.
        
        Aşılama programı mutlaka uygulanmalı ve kayıt tutulmalıdır.
        """,
        "source": "Veteriner Hekim Derneği"
    },
    {
        "category": "sığır",
        "subcategory": "üretim",
        "title": "Süt Sığırı Yetiştiriciliği",
        "content": """
        Süt sığırı yetiştiriciliğinde önemli noktalar:
        
        1. Irk Seçimi: Holstein, Simental gibi yüksek verimli ırklar tercih edilir.
        2. Barınak: Temiz, havalandırmalı, yeterli alan.
        3. Sağım: Düzenli sağım saatleri, hijyen kuralları.
        4. Kayıt Tutma: Süt verimi, sağlık durumu kayıtları.
        5. Beslenme: Laktasyon dönemine göre beslenme programı.
        
        Günlük süt verimi kayıtları tutulmalı ve analiz edilmelidir.
        """,
        "source": "Süt Üreticileri Birliği"
    },
    
    # Kümes Hayvanları
    {
        "category": "kümes_hayvanları",
        "subcategory": "beslenme",
        "title": "Tavuk Beslenme Programı",
        "content": """
        Tavuk beslenmesinde dikkat edilecek konular:
        
        1. Başlangıç Yemi (0-6 hafta): Yüksek protein içerikli starter yem.
        2. Büyütme Yemi (6-18 hafta): Dengeli protein ve enerji.
        3. Yumurta Yemi (18+ hafta): Kalsiyum ve protein açısından zengin.
        4. Su: Sürekli temiz su erişimi.
        5. Yem Miktarı: Yaş ve üretim durumuna göre ayarlanır.
        
        Yem kalitesi ve hijyeni çok önemlidir.
        """,
        "source": "Kümes Hayvanları Yetiştiricileri Derneği"
    },
    {
        "category": "kümes_hayvanları",
        "subcategory": "barınak",
        "title": "Kümes Tasarımı ve Yönetimi",
        "content": """
        Kümes tasarımında önemli faktörler:
        
        1. Alan: Tavuk başına 0.1-0.15 m² alan.
        2. Havalandırma: Doğal ve mekanik havalandırma sistemi.
        3. Aydınlatma: 14-16 saat aydınlatma.
        4. Sıcaklık: 18-22°C optimal sıcaklık.
        5. Nem: %60-70 nem oranı.
        6. Temizlik: Düzenli temizlik ve dezenfeksiyon.
        
        Kümes hijyeni hastalık kontrolü için kritiktir.
        """,
        "source": "Tarım ve Orman Bakanlığı"
    },
    
    # Koyun ve Keçi
    {
        "category": "koyun_keçi",
        "subcategory": "beslenme",
        "title": "Koyun ve Keçi Beslenmesi",
        "content": """
        Koyun ve keçi beslenmesi:
        
        1. Mer'a: Doğal otlaklar en ekonomik besin kaynağı.
        2. Kaba Yem: Kuru ot, saman, silaj.
        3. Kesif Yem: Tahıl, kepek, küspe.
        4. Su: Günde 3-5 litre temiz su.
        5. Tuz: Mineral tuz blokları.
        
        Mer'a döneminde ek yem gereksinimi azalır.
        """,
        "source": "Koyun ve Keçi Yetiştiricileri Birliği"
    },
    {
        "category": "koyun_keçi",
        "subcategory": "üretim",
        "title": "Koyun ve Keçi Üretimi",
        "content": """
        Koyun ve keçi üretiminde dikkat edilecek konular:
        
        1. Çiftleşme: Mevsimsel çiftleşme dönemleri.
        2. Gebelik: 5 ay gebelik süresi.
        3. Doğum: Temiz ve güvenli doğum alanı.
        4. Kuzu/Oğlak Bakımı: İlk süt, aşılama.
        5. Süt Üretimi: Laktasyon dönemi yönetimi.
        
        Doğum öncesi ve sonrası bakım çok önemlidir.
        """,
        "source": "Hayvancılık Araştırma Enstitüsü"
    },
    
    # Genel Hayvancılık
    {
        "category": "genel",
        "subcategory": "barınak",
        "title": "Hayvan Barınakları",
        "content": """
        Hayvan barınaklarında dikkat edilecek konular:
        
        1. Konum: Yüksek, drenajlı, rüzgar korumalı alan.
        2. Yapı: Sağlam, havalandırmalı, aydınlık.
        3. Alan: Hayvan başına yeterli alan.
        4. Zemin: Temizlenebilir, kaymaz zemin.
        5. Su ve Elektrik: Yeterli su ve elektrik tesisatı.
        
        Barınak tasarımı hayvan refahını doğrudan etkiler.
        """,
        "source": "Hayvancılık Genel Müdürlüğü"
    },
    {
        "category": "genel",
        "subcategory": "sağlık",
        "title": "Hayvan Sağlığı ve Aşılama",
        "content": """
        Hayvan sağlığında temel prensipler:
        
        1. Aşılama: Düzenli aşılama programı.
        2. Karantina: Yeni hayvanlar için karantina.
        3. Hijyen: Temizlik ve dezenfeksiyon.
        4. Beslenme: Dengeli ve kaliteli beslenme.
        5. Veteriner Kontrolü: Düzenli sağlık kontrolü.
        
        Hastalık belirtileri erken fark edilmeli ve veteriner çağrılmalıdır.
        """,
        "source": "Veteriner Hekim Odası"
    },
    {
        "category": "genel",
        "subcategory": "ekonomi",
        "title": "Hayvancılık Ekonomisi",
        "content": """
        Hayvancılık işletmesinde ekonomik yönetim:
        
        1. Maliyet Hesabı: Yem, işçilik, sağlık maliyetleri.
        2. Gelir Analizi: Süt, et, yavru satış gelirleri.
        3. Kayıt Tutma: Detaylı mali ve üretim kayıtları.
        4. Pazar Analizi: Fiyat takibi ve pazar araştırması.
        5. Verimlilik: Hayvan başına verim analizi.
        
        Düzenli kayıt tutma başarılı işletme yönetimi için şarttır.
        """,
        "source": "Tarım Ekonomisi Enstitüsü"
    }
]

def seed_livestock_knowledge(db):
    """Seed the database with livestock knowledge data"""
    from app import models
    
    for knowledge_data in LIVESTOCK_KNOWLEDGE_DATA:
        # Check if knowledge already exists
        existing = db.query(models.LivestockKnowledge).filter(
            models.LivestockKnowledge.title == knowledge_data["title"]
        ).first()
        
        if not existing:
            knowledge = models.LivestockKnowledge(**knowledge_data)
            db.add(knowledge)
    
    db.commit()
    print(f"Seeded {len(LIVESTOCK_KNOWLEDGE_DATA)} livestock knowledge entries")

def seed_rag_system():
    """Seed the RAG system with livestock knowledge"""
    from app.rag_system import rag_system
    
    try:
        rag_system.add_documents(LIVESTOCK_KNOWLEDGE_DATA)
        print("RAG system seeded with livestock knowledge")
    except Exception as e:
        print(f"Error seeding RAG system: {e}")

