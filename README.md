# Hayvancılık Sektöründe Yapay Zeka Destekli Sohbet Robotu

Bu proje, hayvancılık sektöründe kullanılmak üzere LangChain ve RAG (Retrieval-Augmented Generation) teknolojileriyle geliştirilmiş yapay zeka destekli bir sohbet robotudur.

## 🎯 Proje Özeti

Bu tez projesi, hayvancılık sektöründe kullanılmak üzere yapay zeka destekli bir sohbet robotu geliştirmeyi amaçlamaktadır. Proje kapsamında:

- **LangChain** ve **RAG** teknolojileri kullanılarak bilgiye erişim sağlanmıştır
- **FastAPI** ile modern bir backend API geliştirilmiştir
- **Kullanıcı yönetim sistemi** ve **admin paneli** entegre edilmiştir
- **Hayvancılık bilgi veritabanı** oluşturulmuştur
- **Modern web arayüzü** ile kullanıcı deneyimi optimize edilmiştir

## 🚀 Özellikler

### Ana Özellikler
- 🤖 **AI Destekli Sohbet**: Hayvancılık konularında uzman yapay zeka asistanı
- 📚 **RAG Teknolojisi**: Retrieval-Augmented Generation ile doğru bilgi erişimi
- 👥 **Kullanıcı Yönetimi**: Kayıt, giriş ve profil yönetimi
- 💬 **Konuşma Geçmişi**: Tüm sohbetlerin kayıt altına alınması
- 🔧 **Admin Paneli**: Sistem yönetimi ve bilgi bankası yönetimi
- 📊 **Analitik**: Kullanım istatistikleri ve raporlama

### Hayvancılık Konuları
- 🐄 **Sığır Yetiştiriciliği**: Beslenme, sağlık, üretim
- 🐔 **Kümes Hayvanları**: Tavuk, hindi yetiştiriciliği
- 🐑 **Koyun ve Keçi**: Mer'a yönetimi, üretim
- 🏠 **Barınak Yönetimi**: Tasarım ve bakım
- 💊 **Sağlık ve Aşılama**: Hastalık kontrolü
- 💰 **Ekonomi**: Maliyet analizi ve verimlilik

## 🛠️ Teknoloji Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM ve veritabanı yönetimi
- **LangChain**: LLM entegrasyonu ve RAG sistemi
- **OpenAI GPT**: Büyük dil modeli
- **ChromaDB**: Vektör veritabanı
- **JWT**: Kimlik doğrulama
- **Pydantic**: Veri validasyonu

### Frontend
- **HTML5/CSS3**: Modern web arayüzü
- **JavaScript**: Dinamik kullanıcı etkileşimi
- **Responsive Design**: Mobil uyumlu tasarım

### Veritabanı
- **SQLite/PostgreSQL**: Ana veritabanı
- **ChromaDB**: Vektör veritabanı (RAG için)

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- pip (Python paket yöneticisi)
- Git

### Adım 1: Projeyi Klonlayın
```bash
git clone <repository-url>
cd livestock-ai-chatbot
```

### Adım 2: Sanal Ortam Oluşturun
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: Ortam Değişkenlerini Ayarlayın
```bash
# env.example dosyasını .env olarak kopyalayın
cp env.example .env

# .env dosyasını düzenleyin ve gerekli değerleri girin
```

### Adım 5: Veritabanını Başlatın
```bash
# Veritabanı tablolarını oluşturun
python -c "from app.database import engine; from app import models; models.Base.metadata.create_all(bind=engine)"
```

### Adım 6: Uygulamayı Başlatın
```bash
python -m app.main
```

Uygulama `http://localhost:8000` adresinde çalışmaya başlayacaktır.

## 🔧 Konfigürasyon



## 📖 Kullanım

### Kullanıcı Arayüzü
1. `http://localhost:8000/chat` adresine gidin
2. Yeni hesap oluşturun veya mevcut hesabınızla giriş yapın
3. Hayvancılık konularında sorularınızı sorun

### Admin Paneli
1. `http://localhost:8000/admin` adresine gidin
2. Admin hesabıyla giriş yapın
3. Kullanıcıları, bilgi bankasını ve sistem istatistiklerini yönetin

### API Dokümantasyonu
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🏗️ Proje Yapısı

```
livestock-ai-chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Ana uygulama
│   ├── config.py              # Konfigürasyon
│   ├── database.py            # Veritabanı bağlantısı
│   ├── models.py              # Veritabanı modelleri
│   ├── schemas.py             # Pydantic şemaları
│   ├── auth.py                # Kimlik doğrulama
│   ├── crud.py                # CRUD işlemleri
│   ├── rag_system.py          # RAG sistemi
│   ├── seed_data.py           # Örnek veriler
│   └── routers/
│       ├── __init__.py
│       ├── auth.py            # Kimlik doğrulama endpoint'leri
│       ├── chat.py            # Sohbet endpoint'leri
│       └── admin.py           # Admin endpoint'leri
├── static/
│   ├── chat.html              # Kullanıcı arayüzü
│   └── admin.html             # Admin paneli
├── requirements.txt           # Python bağımlılıkları
├── env.example               # Örnek ortam değişkenleri
└── README.md                 # Bu dosya
```

## 🔍 API Endpoint'leri

### Kimlik Doğrulama
- `POST /auth/register` - Kullanıcı kaydı
- `POST /auth/login` - Kullanıcı girişi
- `GET /auth/me` - Mevcut kullanıcı bilgisi
- `PUT /auth/me` - Kullanıcı bilgilerini güncelle

### Sohbet
- `POST /chat/send` - Mesaj gönder
- `GET /chat/conversations` - Konuşmaları listele
- `GET /chat/conversations/{id}` - Konuşma detayı
- `GET /chat/conversations/{id}/messages` - Mesajları listele
- `DELETE /chat/conversations/{id}` - Konuşmayı sil

### Admin
- `GET /admin/users` - Kullanıcıları listele
- `POST /admin/users` - Yeni kullanıcı oluştur
- `PUT /admin/users/{id}` - Kullanıcı güncelle
- `DELETE /admin/users/{id}` - Kullanıcı sil
- `GET /admin/knowledge` - Bilgi bankasını listele
- `POST /admin/knowledge` - Yeni bilgi ekle
- `GET /admin/stats` - Sistem istatistikleri

## 🧪 Test Etme

### Manuel Test
1. Uygulamayı başlatın
2. Kullanıcı arayüzünde hesap oluşturun
3. Hayvancılık konularında sorular sorun
4. Admin panelinde bilgi bankasına yeni içerik ekleyin

### API Test
```bash
# Swagger UI kullanarak API'yi test edin
curl -X GET "http://localhost:8000/health"
```

## 🚀 Geliştirme

### Yeni Özellik Ekleme
1. İlgili modeli `models.py`'de tanımlayın
2. Pydantic şemasını `schemas.py`'de oluşturun
3. CRUD işlemlerini `crud.py`'de implement edin
4. API endpoint'lerini ilgili router'da ekleyin
5. Frontend'de gerekli değişiklikleri yapın

### Veritabanı Değişiklikleri
```bash
# Alembic kullanarak migration oluşturun
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

## 📊 Performans

### Optimizasyon Önerileri
- **Caching**: Redis ile API yanıtlarını cache'leyin
- **Database Indexing**: Sık kullanılan alanlar için index oluşturun
- **Vector Database**: ChromaDB performansını optimize edin
- **Load Balancing**: Yüksek trafik için load balancer kullanın

## 🔒 Güvenlik

### Güvenlik Önlemleri
- **JWT Token**: Güvenli kimlik doğrulama
- **Password Hashing**: Bcrypt ile şifre hash'leme
- **Input Validation**: Pydantic ile veri doğrulama
- **CORS**: Cross-origin istekler için güvenlik
- **Rate Limiting**: API rate limiting (önerilen)

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 👥 Yazar

**Proje Geliştiricisi**: Serenay Çelikkaya
**E-posta**: sercelik96@gmail.com
**Üniversite**: Burdur Mehmet Akif Ersoy Üniversitesi
**Bölüm**: Bilgisayar Mühendisliği Yüksek Lisans Programı

## 🙏 Teşekkürler

- **OpenAI** - GPT modeli için
- **LangChain** - RAG implementasyonu için
- **FastAPI** - Modern web framework için
- **Hayvancılık uzmanları** - Bilgi bankası için değerli katkılar

## 📞 İletişim

Sorularınız için:
- **E-posta**: [sercelik96@gmail.com]

---

**Not**: Bu proje eğitim amaçlı geliştirilmiştir. Üretim ortamında kullanmadan önce güvenlik ve performans testlerini yapın.

