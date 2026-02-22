# 4. SİSTEM TASARIMI VE GELİŞTİRME

## 4.1 Sistem Gereksinimleri

### 4.1.1 Fonksiyonel Gereksinimler

#### 4.1.1.1 Kullanıcı Yönetimi

**FR-01: Kullanıcı Kaydı**
- Sistem, yeni kullanıcıların kayıt olmasına izin vermelidir
- Kayıt sırasında e-posta, kullanıcı adı, şifre ve ad soyad bilgileri alınmalıdır
- E-posta adresi benzersiz olmalıdır
- Şifre en az 8 karakter olmalıdır

**FR-02: Kullanıcı Girişi**
- Sistem, kayıtlı kullanıcıların giriş yapmasına izin vermelidir
- Giriş e-posta ve şifre ile yapılmalıdır
- Başarılı giriş sonrası JWT token oluşturulmalıdır
- Token süresi 30 dakika olmalıdır

**FR-03: Profil Yönetimi**
- Kullanıcılar profil bilgilerini güncelleyebilmelidir
- Şifre değiştirme işlemi yapılabilmelidir
- Hesap silme işlemi gerçekleştirilebilmelidir

#### 4.1.1.2 Sohbet Sistemi

**FR-04: Mesaj Gönderme**
- Kullanıcılar hayvancılık konularında sorular sorabilmelidir
- Sistem, sorulara doğru ve güncel yanıtlar vermelidir
- Yanıt süresi 5 saniyeden az olmalıdır
- Yanıtlar Türkçe olmalıdır

**FR-05: Konuşma Geçmişi**
- Sistem, tüm konuşmaları kaydetmelidir
- Kullanıcılar geçmiş konuşmalarını görüntüleyebilmelidir
- Konuşmalar başlık ile kategorize edilmelidir
- Konuşma silme işlemi yapılabilmelidir

**FR-06: Geri Bildirim**
- Kullanıcılar yanıtlara puan verebilmelidir (1-5)
- Yorum ekleme imkanı sağlanmalıdır
- Geri bildirimler sisteme kaydedilmelidir

#### 4.1.1.3 Bilgi Yönetimi

**FR-07: Bilgi Bankası**
- Sistem, hayvancılık konularında kapsamlı bilgi içermelidir
- Bilgiler kategori ve alt kategori bazında organize edilmelidir
- Bilgi güncelleme işlemi yapılabilmelidir
- Yeni bilgi ekleme imkanı sağlanmalıdır

**FR-08: Arama Sistemi**
- Kullanıcılar bilgi bankasında arama yapabilmelidir
- Arama sonuçları ilgili sıraya göre listelenmelidir
- Filtreleme seçenekleri sunulmalıdır

#### 4.1.1.4 Admin Paneli

**FR-09: Kullanıcı Yönetimi**
- Admin kullanıcıları görüntüleyebilmelidir
- Kullanıcı bilgilerini düzenleyebilmelidir
- Kullanıcı hesaplarını silebilmelidir
- Kullanıcı istatistiklerini görüntüleyebilmelidir

**FR-10: İçerik Yönetimi**
- Admin bilgi bankasına yeni içerik ekleyebilmelidir
- Mevcut içerikleri düzenleyebilmelidir
- İçerikleri silebilmelidir
- İçerik kategorilerini yönetebilmelidir

**FR-11: Sistem İstatistikleri**
- Günlük, haftalık, aylık istatistikler görüntülenebilmelidir
- Kullanıcı aktivite raporları oluşturulabilmelidir
- Sistem performans metrikleri izlenebilmelidir

### 4.1.2 Non-Fonksiyonel Gereksinimler

#### 4.1.2.1 Performans Gereksinimleri

**NFR-01: Yanıt Süresi**
- API yanıt süresi 2 saniyeden az olmalıdır
- Chat yanıt süresi 5 saniyeden az olmalıdır
- Sayfa yükleme süresi 3 saniyeden az olmalıdır

**NFR-02: Throughput**
- Sistem aynı anda 100 kullanıcıyı destekleyebilmelidir
- Saniyede 50 istek işleyebilmelidir
- Veritabanı sorguları 1 saniyeden az sürmelidir

**NFR-03: Ölçeklenebilirlik**
- Kullanıcı sayısı artışına uyum sağlayabilmelidir
- Veri hacmi artışına uyum sağlayabilmelidir
- Horizontal scaling desteklemelidir

#### 4.1.2.2 Güvenlik Gereksinimleri

**NFR-04: Kimlik Doğrulama**
- JWT tabanlı güvenli kimlik doğrulama
- Şifre hash'leme (bcrypt)
- Session timeout (30 dakika)
- Rate limiting (dakikada 60 istek)

**NFR-05: Veri Güvenliği**
- HTTPS ile veri iletimi
- SQL injection koruması
- XSS koruması
- CSRF koruması

**NFR-06: Erişim Kontrolü**
- Role-based access control
- Admin yetkileri
- API endpoint koruması
- Veri erişim kontrolü

#### 4.1.2.3 Kullanılabilirlik Gereksinimleri

**NFR-07: Kullanıcı Arayüzü**
- Responsive tasarım (mobil uyumlu)
- Modern ve kullanıcı dostu arayüz
- Erişilebilirlik standartları (WCAG 2.1)
- Çoklu tarayıcı desteği

**NFR-08: Kullanılabilirlik**
- Öğrenme eğrisi düşük olmalıdır
- Hata mesajları açık ve anlaşılır olmalıdır
- Yardım dokümantasyonu sağlanmalıdır
- Kullanıcı rehberi bulunmalıdır

#### 4.1.2.4 Güvenilirlik Gereksinimleri

**NFR-09: Uptime**
- Sistem %99.5 uptime sağlamalıdır
- Planlı bakım süresi aylık 4 saatten az olmalıdır
- Hata kurtarma süresi 1 saatten az olmalıdır

**NFR-10: Veri Bütünlüğü**
- Veri kaybı olmamalıdır
- Backup stratejisi uygulanmalıdır
- Transaction güvenliği sağlanmalıdır
- Veri tutarlılığı korunmalıdır

## 4.2 Veritabanı Tasarımı

### 4.2.1 Veritabanı Mimarisi

Sistem, **ilişkisel veritabanı** ve **vektör veritabanı** olmak üzere iki farklı veritabanı kullanmaktadır:

#### 4.2.1.1 İlişkisel Veritabanı (SQLite/PostgreSQL)

**Amaç:**
- Kullanıcı bilgileri
- Konuşma geçmişi
- Sistem logları
- Yapılandırılmış veriler

**Özellikler:**
- ACID uyumluluğu
- İlişkisel veri bütünlüğü
- Transaction desteği
- Backup ve recovery

#### 4.2.1.2 Vektör Veritabanı (ChromaDB)

**Amaç:**
- Hayvancılık bilgi tabanı
- Embedding'ler
- Benzerlik araması
- RAG sistemi

**Özellikler:**
- Yüksek boyutlu vektör desteği
- Hızlı benzerlik araması
- Ölçeklenebilirlik
- Persistence

### 4.2.2 Veritabanı Şeması

#### 4.2.2.1 Kullanıcı Tablosu (Users)

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Açıklama:**
- Kullanıcı temel bilgileri
- Kimlik doğrulama bilgileri
- Yetki seviyeleri
- Zaman damgaları

#### 4.2.2.2 Konuşma Tablosu (Conversations)

```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**Açıklama:**
- Kullanıcı konuşmaları
- Konuşma başlıkları
- İlişkisel bağlantılar

#### 4.2.2.3 Mesaj Tablosu (Messages)

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    is_user BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);
```

**Açıklama:**
- Konuşma mesajları
- Kullanıcı ve bot mesajları
- İçerik saklama

#### 4.2.2.4 Hayvancılık Bilgi Tablosu (Livestock_Knowledge)

```sql
CREATE TABLE livestock_knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category VARCHAR(100) NOT NULL,
    subcategory VARCHAR(100),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    source VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Açıklama:**
- Hayvancılık bilgi tabanı
- Kategorize edilmiş içerik
- Kaynak bilgileri

#### 4.2.2.5 Geri Bildirim Tablosu (Feedback)

```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    conversation_id INTEGER NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);
```

**Açıklama:**
- Kullanıcı geri bildirimleri
- Puanlama sistemi
- Yorum alanı

#### 4.2.2.6 Analitik Tablosu (Analytics)

```sql
CREATE TABLE analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    total_conversations INTEGER DEFAULT 0,
    total_messages INTEGER DEFAULT 0,
    total_users INTEGER DEFAULT 0,
    avg_response_time FLOAT DEFAULT 0.0,
    popular_topics TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Açıklama:**
- Sistem istatistikleri
- Performans metrikleri
- Trend analizi

### 4.2.3 İndeksleme Stratejisi

#### 4.2.3.1 Performans İndeksleri

```sql
-- Kullanıcı e-posta indeksi
CREATE INDEX idx_users_email ON users(email);

-- Konuşma kullanıcı indeksi
CREATE INDEX idx_conversations_user_id ON conversations(user_id);

-- Mesaj konuşma indeksi
CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);

-- Bilgi kategori indeksi
CREATE INDEX idx_livestock_knowledge_category ON livestock_knowledge(category);

-- Geri bildirim kullanıcı indeksi
CREATE INDEX idx_feedback_user_id ON feedback(user_id);

-- Analitik tarih indeksi
CREATE INDEX idx_analytics_date ON analytics(date);
```

#### 4.2.3.2 Arama İndeksleri

```sql
-- Tam metin arama indeksi
CREATE INDEX idx_livestock_knowledge_content_fts ON livestock_knowledge USING gin(to_tsvector('turkish', content));

-- Başlık arama indeksi
CREATE INDEX idx_livestock_knowledge_title_fts ON livestock_knowledge USING gin(to_tsvector('turkish', title));
```

## 4.3 API Geliştirme

### 4.3.1 API Mimarisi

#### 4.3.1.1 RESTful API Tasarımı

Sistem, **REST (Representational State Transfer)** prensiplerine uygun olarak tasarlanmıştır:

**Temel Prensipler:**
- Stateless: Her istek bağımsızdır
- Client-Server: Ayrı katmanlar
- Cacheable: Önbellekleme desteği
- Uniform Interface: Standart arayüz
- Layered System: Katmanlı yapı

#### 4.3.1.2 API Endpoint Yapısı

```
Base URL: https://api.livestock-ai.com/v1

Authentication:
POST /auth/register
POST /auth/login
GET  /auth/me
PUT  /auth/me

Chat:
POST /chat/send
GET  /chat/conversations
GET  /chat/conversations/{id}
GET  /chat/conversations/{id}/messages
DELETE /chat/conversations/{id}
POST /chat/feedback

Admin:
GET  /admin/users
POST /admin/users
PUT  /admin/users/{id}
DELETE /admin/users/{id}
GET  /admin/knowledge
POST /admin/knowledge
PUT  /admin/knowledge/{id}
DELETE /admin/knowledge/{id}
GET  /admin/analytics
GET  /admin/stats

Health:
GET  /health
```

### 4.3.2 API Geliştirme Süreci

#### 4.3.2.1 FastAPI Framework Kullanımı

**Avantajlar:**
- Otomatik API dokümantasyonu
- Tip güvenliği (Pydantic)
- Asenkron programlama
- Yüksek performans
- Modern Python özellikleri

**Temel Yapı:**
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

app = FastAPI(
    title="Hayvancılık AI Sohbet Robotu",
    description="LangChain ve RAG teknolojileriyle geliştirilmiş sistem",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 4.3.2.2 Dependency Injection

**Veritabanı Bağımlılığı:**
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Kullanım
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)
```

**Kimlik Doğrulama Bağımlılığı:**
```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user
```

### 4.3.3 API Endpoint Geliştirme

#### 4.3.3.1 Kimlik Doğrulama Endpoint'leri

**Kullanıcı Kaydı:**
```python
@app.post("/auth/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # E-posta kontrolü
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Kullanıcı oluşturma
    return crud.create_user(db=db, user=user)
```

**Kullanıcı Girişi:**
```python
@app.post("/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
```

#### 4.3.3.2 Chat Endpoint'leri

**Mesaj Gönderme:**
```python
@app.post("/chat/send", response_model=ChatResponse)
def send_message(
    chat_request: ChatRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    # Konuşma oluşturma/güncelleme
    if not chat_request.conversation_id:
        conversation = crud.create_conversation(
            db=db,
            conversation=ConversationCreate(title=chat_request.message[:50]),
            user_id=current_user.id
        )
        conversation_id = conversation.id
    else:
        conversation_id = chat_request.conversation_id
    
    # Kullanıcı mesajını kaydetme
    user_message = crud.create_message(
        db=db,
        message=MessageCreate(
            content=chat_request.message,
            is_user=True,
            conversation_id=conversation_id
        )
    )
    
    # AI yanıtı alma
    ai_response = rag_system.query(chat_request.message)
    
    # AI yanıtını kaydetme
    ai_message = crud.create_message(
        db=db,
        message=MessageCreate(
            content=ai_response["answer"],
            is_user=False,
            conversation_id=conversation_id
        )
    )
    
    return ChatResponse(
        response=ai_response["answer"],
        conversation_id=conversation_id,
        message_id=ai_message.id
    )
```

#### 4.3.3.3 Admin Endpoint'leri

**Kullanıcı Yönetimi:**
```python
@app.get("/admin/users", response_model=List[User])
def get_all_users(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    return crud.get_users(db=db, skip=skip, limit=limit)

@app.post("/admin/users", response_model=User)
def create_user(
    user: UserCreate,
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    return crud.create_user(db=db, user=user)
```

### 4.3.4 Hata Yönetimi

#### 4.3.4.1 HTTP Hata Kodları

**4xx Client Errors:**
- 400 Bad Request: Geçersiz istek
- 401 Unauthorized: Kimlik doğrulama gerekli
- 403 Forbidden: Yetki yetersiz
- 404 Not Found: Kaynak bulunamadı
- 422 Unprocessable Entity: Validasyon hatası

**5xx Server Errors:**
- 500 Internal Server Error: Sunucu hatası
- 502 Bad Gateway: Gateway hatası
- 503 Service Unavailable: Servis kullanılamıyor

#### 4.3.4.2 Hata Yönetimi Implementasyonu

```python
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

# Özel hata sınıfları
class ValidationError(Exception):
    def __init__(self, message: str):
        self.message = message

# Global hata yakalayıcı
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.message}
    )

# Hata yanıt formatı
{
    "detail": "Hata mesajı",
    "error_code": "ERROR_CODE",
    "timestamp": "2024-01-01T00:00:00Z"
}
```

## 4.4 RAG Sistemi Entegrasyonu

### 4.4.1 RAG Sistemi Mimarisi

#### 4.4.1.1 Sistem Bileşenleri

**1. Belge İşleme Modülü:**
- Kaynak belgelerin yüklenmesi
- Metin temizleme ve normalizasyon
- Belge parçalama (chunking)
- Metadata ekleme

**2. Embedding Modülü:**
- Metin vektörleştirme
- Embedding modeli yönetimi
- Vektör optimizasyonu
- Batch işleme

**3. Vektör Veritabanı:**
- Embedding saklama
- Benzerlik araması
- İndeksleme
- Performans optimizasyonu

**4. Retrieval Modülü:**
- Sorgu işleme
- Benzerlik hesaplama
- Sonuç filtreleme
- Ranking

**5. Generation Modülü:**
- LLM entegrasyonu
- Prompt engineering
- Yanıt üretimi
- Kalite kontrolü

#### 4.4.1.2 Veri Akışı

```
Kaynak Belge → Belge İşleme → Embedding → Vektör DB
                                    ↓
Kullanıcı Sorgusu → Embedding → Benzerlik Araması → İlgili Belge
                                    ↓
İlgili Belge + Sorgu → LLM → Yanıt Üretimi → Kullanıcı
```

### 4.4.2 LangChain Entegrasyonu

#### 4.4.2.1 LangChain Bileşenleri

**Document Loader:**
```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Belge yükleme
loader = TextLoader("livestock_knowledge.txt")
documents = loader.load()

# Metin parçalama
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = text_splitter.split_documents(documents)
```

**Embedding Model:**
```python
from langchain.embeddings import HuggingFaceEmbeddings

# Embedding modeli
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)
```

**Vector Store:**
```python
from langchain.vectorstores import Chroma

# Vektör veritabanı
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

**Retrieval QA:**
```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# QA zinciri
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=OPENAI_API_KEY),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
    return_source_documents=True
)
```

#### 4.4.2.2 Özel Prompt Template

```python
from langchain.prompts import PromptTemplate

# Hayvancılık özel prompt
prompt_template = """
Sen hayvancılık sektöründe uzman bir yapay zeka asistanısın. 
Aşağıdaki bağlamı kullanarak soruları Türkçe olarak yanıtla.

Bağlam:
{context}

Soru: {question}

Yanıt: Hayvancılık konusunda size yardımcı olmak için aşağıdaki bilgileri paylaşıyorum:

"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)
```

### 4.4.3 Hayvancılık Bilgi Tabanı

#### 4.4.3.1 Bilgi Kategorileri

**Sığır Yetiştiriciliği:**
- Beslenme: Yem programları, besin gereksinimleri
- Sağlık: Hastalıklar, aşılama, tedavi
- Üretim: Süt üretimi, et üretimi, üreme
- Barınak: Ahır tasarımı, havalandırma, temizlik

**Kümes Hayvanları:**
- Beslenme: Yem formülasyonu, beslenme programları
- Sağlık: Hastalık kontrolü, aşılama programları
- Üretim: Yumurta üretimi, et üretimi
- Barınak: Kümes tasarımı, çevre kontrolü

**Koyun ve Keçi:**
- Beslenme: Mer'a yönetimi, yem programları
- Sağlık: Parazit kontrolü, hastalık yönetimi
- Üretim: Yün üretimi, süt üretimi, üreme
- Barınak: Ağıl tasarımı, çevre yönetimi

#### 4.4.3.2 Bilgi Kalite Kontrolü

**Uzman Doğrulaması:**
- Veteriner hekim onayı
- Hayvancılık uzmanı kontrolü
- Akademik kaynak doğrulaması
- Pratik uygulama testi

**Güncellik Kontrolü:**
- Düzenli bilgi güncelleme
- Kaynak takibi
- Versiyon kontrolü
- Değişiklik logları

### 4.4.4 Performans Optimizasyonu

#### 4.4.4.1 Embedding Optimizasyonu

**Model Seçimi:**
- Türkçe dil desteği
- Hızlı işleme
- Yüksek kalite
- Küçük boyut

**Batch İşleme:**
```python
# Toplu embedding oluşturma
def create_embeddings_batch(texts, batch_size=32):
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        batch_embeddings = embedding_model.encode(batch)
        embeddings.extend(batch_embeddings)
    return embeddings
```

#### 4.4.4.2 Vektör Araması Optimizasyonu

**İndeksleme:**
```python
# HNSW indeksi
vectorstore = Chroma(
    collection_name="livestock_knowledge",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Arama parametreleri
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4, "score_threshold": 0.7}
)
```

**Caching:**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_similarity_search(query: str, k: int = 4):
    return vectorstore.similarity_search(query, k=k)
```

## 4.5 Kullanıcı Arayüzü Geliştirme

### 4.5.1 Frontend Mimarisi

#### 4.5.1.1 Teknoloji Seçimi

**HTML5:**
- Semantik markup
- Accessibility desteği
- Modern web standartları
- SEO optimizasyonu

**CSS3:**
- Responsive tasarım
- Modern layout (Flexbox, Grid)
- Animasyonlar ve geçişler
- Dark/Light mode desteği

**JavaScript (Vanilla):**
- Modern ES6+ özellikleri
- Asenkron programlama (async/await)
- DOM manipülasyonu
- API entegrasyonu

#### 4.5.1.2 Responsive Tasarım

**Mobile-First Yaklaşım:**
```css
/* Mobile styles (default) */
.chat-container {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Tablet styles */
@media (min-width: 768px) {
    .chat-container {
        width: 90%;
        max-width: 800px;
        height: 90vh;
        margin: 0 auto;
    }
}

/* Desktop styles */
@media (min-width: 1024px) {
    .chat-container {
        max-width: 1000px;
    }
}
```

### 4.5.2 Chat Arayüzü Geliştirme

#### 4.5.2.1 Arayüz Bileşenleri

**Chat Container:**
```html
<div class="chat-container">
    <div class="chat-header">
        <h1>🐄 Hayvancılık AI Asistanı</h1>
        <p>Size hayvancılık konularında yardımcı olmaya hazırım!</p>
    </div>
    
    <div class="chat-messages" id="chatMessages">
        <!-- Mesajlar burada görüntülenir -->
    </div>
    
    <div class="chat-input">
        <input type="text" id="messageInput" placeholder="Hayvancılık hakkında bir soru sorun...">
        <button id="sendBtn">Gönder</button>
    </div>
</div>
```

**Mesaj Bileşeni:**
```html
<div class="message user">
    <div class="message-content">
        Kullanıcı mesajı
    </div>
</div>

<div class="message bot">
    <div class="message-content">
        AI yanıtı
    </div>
</div>
```

#### 4.5.2.2 JavaScript Fonksiyonları

**Mesaj Gönderme:**
```javascript
async function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Kullanıcı mesajını ekle
    addMessageToChat(message, true);
    input.value = '';
    
    // Loading göster
    showLoading();
    
    try {
        // API'ye istek gönder
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            },
            body: JSON.stringify({
                message: message,
                user_id: getCurrentUserId()
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            addMessageToChat(data.response, false);
        } else {
            addMessageToChat('Üzgünüm, bir hata oluştu.', false);
        }
    } catch (error) {
        addMessageToChat('Bağlantı hatası.', false);
    } finally {
        hideLoading();
    }
}
```

**Mesaj Ekleme:**
```javascript
function addMessageToChat(content, isUser) {
    const container = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;
    
    messageDiv.appendChild(contentDiv);
    container.appendChild(messageDiv);
    container.scrollTop = container.scrollHeight;
}
```

### 4.5.3 Admin Paneli Geliştirme

#### 4.5.3.1 Panel Bileşenleri

**Dashboard:**
```html
<div class="admin-dashboard">
    <div class="stats-grid">
        <div class="stat-card">
            <h3 id="totalUsers">-</h3>
            <p>Toplam Kullanıcı</p>
        </div>
        <div class="stat-card">
            <h3 id="totalConversations">-</h3>
            <p>Toplam Konuşma</p>
        </div>
        <div class="stat-card">
            <h3 id="totalMessages">-</h3>
            <p>Toplam Mesaj</p>
        </div>
    </div>
</div>
```

**Kullanıcı Yönetimi:**
```html
<div class="user-management">
    <table class="users-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Kullanıcı Adı</th>
                <th>E-posta</th>
                <th>Admin</th>
                <th>İşlemler</th>
            </tr>
        </thead>
        <tbody id="usersTableBody">
            <!-- Kullanıcılar burada listelenir -->
        </tbody>
    </table>
</div>
```

#### 4.5.3.2 Admin Fonksiyonları

**Kullanıcı Listeleme:**
```javascript
async function loadUsers() {
    try {
        const response = await fetch('/admin/users', {
            headers: {
                'Authorization': `Bearer ${getAdminToken()}`
            }
        });
        
        if (response.ok) {
            const users = await response.json();
            displayUsers(users);
        }
    } catch (error) {
        console.error('Error loading users:', error);
    }
}

function displayUsers(users) {
    const tbody = document.getElementById('usersTableBody');
    tbody.innerHTML = '';
    
    users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.email}</td>
            <td>${user.is_admin ? 'Evet' : 'Hayır'}</td>
            <td>
                <button onclick="editUser(${user.id})">Düzenle</button>
                <button onclick="deleteUser(${user.id})">Sil</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}
```

### 4.5.4 Kullanıcı Deneyimi Optimizasyonu

#### 4.5.4.1 Performans Optimizasyonu

**Lazy Loading:**
```javascript
// Konuşma geçmişi lazy loading
function loadConversations(page = 1, limit = 20) {
    return fetch(`/chat/conversations?page=${page}&limit=${limit}`)
        .then(response => response.json());
}

// Infinite scroll
let currentPage = 1;
const loadMoreBtn = document.getElementById('loadMore');

loadMoreBtn.addEventListener('click', async () => {
    currentPage++;
    const conversations = await loadConversations(currentPage);
    appendConversations(conversations);
});
```

**Caching:**
```javascript
// Local storage cache
const cache = {
    set: (key, value) => {
        localStorage.setItem(key, JSON.stringify(value));
    },
    get: (key) => {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    }
};

// Cache kullanımı
function getCachedUser() {
    let user = cache.get('currentUser');
    if (!user) {
        user = await fetchCurrentUser();
        cache.set('currentUser', user);
    }
    return user;
}
```

#### 4.5.4.2 Accessibility

**ARIA Labels:**
```html
<button id="sendBtn" aria-label="Mesaj gönder">
    Gönder
</button>

<input type="text" id="messageInput" 
       aria-label="Mesaj girişi" 
       aria-describedby="messageHelp">
<div id="messageHelp">Hayvancılık konularında sorularınızı yazabilirsiniz</div>
```

**Keyboard Navigation:**
```javascript
// Enter tuşu ile mesaj gönderme
document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Tab navigation
document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
        // Tab order yönetimi
    }
});
```

Bu bölümde, sistem tasarımı ve geliştirme sürecinin tüm aşamaları detaylı olarak açıklanmıştır. Bir sonraki bölümde, uygulama ve test sonuçları ele alınacaktır.

