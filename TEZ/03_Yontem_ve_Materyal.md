# 3. YÖNTEM VE MATERYAL

## 3.1 Giriş

Bu bölümde, yapay zeka destekli akıllı çiftlik yönetim sisteminin geliştirilmesi için kullanılan yöntemler, teknolojiler ve araçlar detaylı olarak açıklanmaktadır. Sistem, modern yazılım geliştirme metodolojileri ve en güncel teknolojiler kullanılarak tasarlanmıştır.

## 3.2 Araştırma Yöntemi

### 3.2.1 Geliştirme Metodolojisi

Sistem geliştirme sürecinde **Agile/Scrum** metodolojisi benimsenmiştir. Bu metodoloji, hızlı prototipleme, sürekli geri bildirim ve iteratif geliştirme sağlamaktadır. Proje, 2 haftalık sprint'ler halinde organize edilmiş ve her sprint sonunda test edilebilir özellikler teslim edilmiştir.

### 3.2.2 Sistem Geliştirme Yaşam Döngüsü

1. **Gereksinim Analizi**: Çiftlik sahipleri ve veteriner hekimlerle görüşmeler
2. **Sistem Tasarımı**: Mimari tasarım ve veri modeli oluşturma
3. **Prototipleme**: Hızlı prototip geliştirme ve kullanıcı geri bildirimi
4. **Geliştirme**: Kod yazma ve test etme
5. **Test**: Birim testleri, entegrasyon testleri ve kullanıcı kabul testleri
6. **Deployment**: Canlı sisteme yükleme ve izleme

## 3.3 Teknoloji Stack'i

### 3.3.1 Backend Teknolojileri

#### 3.3.1.1 FastAPI Framework

**FastAPI** modern, hızlı (yüksek performanslı) bir web framework'üdür. Python 3.7+ için API'ler oluşturmak üzere tasarlanmıştır. Seçilme nedenleri:

- **Yüksek Performans**: NodeJS ve Go ile karşılaştırılabilir hız
- **Otomatik Dokümantasyon**: OpenAPI/Swagger entegrasyonu
- **Tip Güvenliği**: Python type hints ile güçlü tip kontrolü
- **Modern Python**: Python 3.7+ özelliklerini tam destekleme
- **Kolay Test**: Test yazmayı kolaylaştıran yapı

```python
# FastAPI örnek kullanım
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI(title="Smart Farm API", version="1.0.0")

class FarmCreate(BaseModel):
    name: str
    location: str
    farm_type: str

@app.post("/farms/")
async def create_farm(farm: FarmCreate):
    return {"message": "Farm created successfully"}
```

#### 3.3.1.2 SQLAlchemy ORM

**SQLAlchemy**, Python için güçlü bir Object-Relational Mapping (ORM) kütüphanesidir. Seçilme nedenleri:

- **Veritabanı Bağımsızlığı**: Farklı veritabanları arasında kolay geçiş
- **Güçlü Sorgu API'si**: Karmaşık sorguları kolayca yazabilme
- **İlişkisel Veri Modeli**: Foreign key'ler ve join'ler için mükemmel destek
- **Migration Desteği**: Alembic ile veritabanı şema yönetimi

```python
# SQLAlchemy model örneği
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Farm(Base):
    __tablename__ = "farms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    farm_type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    animals = relationship("Animal", back_populates="farm")
```

#### 3.3.1.3 JWT Authentication

**JSON Web Token (JWT)** tabanlı authentication sistemi kullanılmıştır. Seçilme nedenleri:

- **Stateless**: Sunucu tarafında session bilgisi tutmaya gerek yok
- **Ölçeklenebilirlik**: Mikroservis mimarisi için uygun
- **Güvenlik**: Token imzalama ve şifreleme desteği
- **Standart**: RFC 7519 standardına uygunluk

```python
# JWT token oluşturma örneği
from jose import JWTError, jwt
from datetime import datetime, timedelta

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

### 3.3.2 Veritabanı Teknolojileri

#### 3.3.2.1 SQLite

Geliştirme ve test aşamasında **SQLite** veritabanı kullanılmıştır. Seçilme nedenleri:

- **Sıfır Konfigürasyon**: Kurulum ve yapılandırma gerektirmez
- **Hafiflik**: Tek dosya veritabanı
- **Hızlı Geliştirme**: Prototipleme için ideal
- **SQL Uyumluluğu**: Standart SQL sorguları destekler

#### 3.3.2.2 PostgreSQL (Production)

Canlı sistemde **PostgreSQL** kullanılmıştır. Seçilme nedenleri:

- **Güvenilirlik**: ACID uyumluluğu ve veri bütünlüğü
- **Performans**: Büyük veri setleri için optimize edilmiş
- **Ölçeklenebilirlik**: Yüksek eşzamanlı kullanıcı desteği
- **JSON Desteği**: NoSQL özellikler de destekler

### 3.3.3 AI ve Machine Learning Teknolojileri

#### 3.3.3.1 RAG (Retrieval-Augmented Generation)

**RAG teknolojisi**, büyük dil modellerini harici bilgi kaynakları ile güçlendiren bir yaklaşımdır. Sistem mimarisi:

1. **Document Store**: Hayvancılık bilgi tabanı
2. **Embedding Model**: Metinleri vektörlere dönüştürme
3. **Vector Database**: Benzerlik araması için vektör depolama
4. **LLM Integration**: Büyük dil modeli ile yanıt üretimi

```python
# RAG sistem örneği
from sentence_transformers import SentenceTransformer
import chromadb

class RAGSystem:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection("livestock_knowledge")
    
    def query(self, question: str) -> str:
        # Soruyu vektöre dönüştür
        query_embedding = self.embedder.encode([question])
        
        # Benzer dokümanları bul
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=5
        )
        
        # LLM ile yanıt üret
        context = " ".join(results['documents'][0])
        response = self.generate_response(question, context)
        return response
```

#### 3.3.3.2 Sentence Transformers

**Sentence Transformers** kütüphanesi, metinleri yüksek boyutlu vektörlere dönüştürmek için kullanılmıştır. Model seçimi:

- **Model**: `all-MiniLM-L6-v2`
- **Boyut**: 384 boyutlu vektörler
- **Dil Desteği**: Çok dilli destek
- **Performans**: Hızlı ve hafif model

#### 3.3.3.3 ChromaDB

**ChromaDB**, vektör veritabanı olarak kullanılmıştır. Seçilme nedenleri:

- **Açık Kaynak**: Ücretsiz ve açık kaynak
- **Python Entegrasyonu**: Kolay entegrasyon
- **Performans**: Hızlı benzerlik araması
- **Ölçeklenebilirlik**: Büyük vektör koleksiyonları destekler

### 3.3.4 Frontend Teknolojileri

#### 3.3.4.1 HTML5, CSS3, JavaScript

Modern web standartları kullanılarak responsive ve kullanıcı dostu arayüz geliştirilmiştir:

- **HTML5**: Semantik markup ve modern özellikler
- **CSS3**: Flexbox, Grid, animasyonlar ve responsive tasarım
- **Vanilla JavaScript**: Framework bağımlılığı olmadan modern JavaScript

```html
<!-- Modern HTML5 yapısı -->
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akıllı Çiftlik Yönetim Sistemi</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🏡 Akıllı Çiftlik Yönetim Sistemi</h1>
        </header>
        <main class="main-content">
            <!-- İçerik -->
        </main>
    </div>
    <script src="app.js"></script>
</body>
</html>
```

#### 3.3.4.2 Responsive Design

Mobil-first yaklaşımı ile responsive tasarım uygulanmıştır:

```css
/* Responsive CSS örneği */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
    
    .dashboard {
        grid-template-columns: 1fr;
    }
}
```

### 3.3.5 Cloud ve Deployment Teknolojileri

#### 3.3.5.1 Railway Platform

**Railway** cloud platformu kullanılmıştır. Seçilme nedenleri:

- **Kolay Deployment**: Git push ile otomatik deployment
- **Otomatik Scaling**: Trafiğe göre otomatik ölçeklendirme
- **Database Desteği**: PostgreSQL ve Redis desteği
- **Custom Domain**: Özel domain desteği
- **SSL**: Otomatik SSL sertifikası

#### 3.3.5.2 Docker Containerization

**Docker** ile containerization yapılmıştır:

```dockerfile
# Dockerfile örneği
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 3.4 Veri Toplama ve Hazırlama

### 3.4.1 Hayvancılık Bilgi Tabanı

Hayvancılık konusunda kapsamlı bir bilgi tabanı oluşturulmuştur:

#### 3.4.1.1 Veri Kaynakları

1. **Akademik Makaleler**: Hayvancılık ve veteriner hekimlik dergileri
2. **Resmi Kaynaklar**: Tarım ve Orman Bakanlığı yayınları
3. **Uzman Görüşleri**: Veteriner hekim ve zooteknist görüşleri
4. **Pratik Deneyimler**: Çiftlik sahiplerinin deneyimleri

#### 3.4.1.2 Veri Kategorileri

- **Hayvan Sağlığı**: Hastalıklar, aşılar, tedavi yöntemleri
- **Beslenme**: Yem türleri, beslenme programları, besin değerleri
- **Üretim**: Süt, et, yumurta üretim optimizasyonu
- **Genetik**: Irk seçimi, üreme programları
- **Çevre**: Barınak koşulları, havalandırma, sıcaklık kontrolü

### 3.4.2 Test Verileri

Sistem testi için gerçekçi test verileri oluşturulmuştur:

```python
# Test verisi oluşturma örneği
test_farms = [
    {
        "name": "Test Çiftliği",
        "location": "Ankara, Türkiye",
        "farm_type": "cattle",
        "total_area": 100.0
    }
]

test_animals = [
    {
        "tag_number": "001",
        "name": "Bella",
        "species": "cattle",
        "breed": "Holstein",
        "gender": "female",
        "birth_date": "2020-03-15",
        "weight": 450.0,
        "status": "active"
    }
]
```

## 3.5 Geliştirme Araçları

### 3.5.1 IDE ve Editörler

- **Visual Studio Code**: Ana geliştirme ortamı
- **Git**: Versiyon kontrol sistemi
- **GitHub**: Kod deposu ve işbirliği platformu

### 3.5.2 Test Araçları

- **pytest**: Python test framework'ü
- **Postman**: API test aracı
- **Selenium**: Web arayüz testleri

### 3.5.3 Monitoring ve Logging

- **Railway Logs**: Sistem logları
- **FastAPI Logging**: Uygulama logları
- **Error Tracking**: Hata takibi ve raporlama

## 3.6 Performans Optimizasyonu

### 3.6.1 Veritabanı Optimizasyonu

- **Indexing**: Sık kullanılan alanlar için index'ler
- **Query Optimization**: Verimli SQL sorguları
- **Connection Pooling**: Veritabanı bağlantı havuzu

### 3.6.2 API Optimizasyonu

- **Caching**: Redis ile önbellekleme
- **Pagination**: Büyük veri setleri için sayfalama
- **Async Operations**: Asenkron işlemler

### 3.6.3 Frontend Optimizasyonu

- **Lazy Loading**: Gerektiğinde yükleme
- **Image Optimization**: Görsel optimizasyonu
- **Minification**: CSS ve JavaScript sıkıştırma

## 3.7 Güvenlik Önlemleri

### 3.7.1 Authentication ve Authorization

- **JWT Tokens**: Güvenli token tabanlı kimlik doğrulama
- **Password Hashing**: bcrypt ile şifre hash'leme
- **Role-based Access**: Rol tabanlı erişim kontrolü

### 3.7.2 API Güvenliği

- **CORS**: Cross-Origin Resource Sharing kontrolü
- **Rate Limiting**: API rate limiting
- **Input Validation**: Girdi doğrulama ve sanitizasyon

### 3.7.3 Veri Güvenliği

- **HTTPS**: SSL/TLS şifreleme
- **Environment Variables**: Hassas bilgilerin güvenli saklanması
- **Database Encryption**: Veritabanı şifreleme

## 3.8 Test Stratejisi

### 3.8.1 Test Türleri

1. **Unit Tests**: Bireysel fonksiyon testleri
2. **Integration Tests**: Bileşen entegrasyon testleri
3. **API Tests**: REST API endpoint testleri
4. **User Acceptance Tests**: Kullanıcı kabul testleri

### 3.8.2 Test Verileri

- **Mock Data**: Test için sahte veriler
- **Real Data**: Gerçek çiftlik verileri (anonimleştirilmiş)
- **Edge Cases**: Sınır durumları test verileri

## 3.9 Sonuç

Bu bölümde, sistem geliştirme sürecinde kullanılan tüm teknolojiler, araçlar ve yöntemler detaylı olarak açıklanmıştır. Modern yazılım geliştirme standartları ve en güncel teknolojiler kullanılarak, ölçeklenebilir, güvenli ve kullanıcı dostu bir sistem geliştirilmiştir.

Seçilen teknoloji stack'i, sistemin performans, güvenlik ve kullanılabilirlik gereksinimlerini karşılayacak şekilde optimize edilmiştir. Açık kaynak teknolojilerin tercih edilmesi, sistemin sürdürülebilirliğini ve topluluk desteğini artırmaktadır.


