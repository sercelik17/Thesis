# 3. YÖNTEM VE MATERYAL

## 3.1 Araştırma Yöntemi

### 3.1.1 Araştırma Tasarımı

Bu çalışma, **geliştirme araştırması (Development Research)** yöntemi kullanılarak gerçekleştirilmiştir. Geliştirme araştırması, yeni bir ürün, sistem veya süreç geliştirmek ve bu geliştirilen ürünün etkinliğini test etmek amacıyla yapılan araştırma türüdür (Richey & Klein, 2007).

Araştırma süreci aşağıdaki aşamalardan oluşmaktadır:

1. **Analiz Aşaması**: Problem tanımı ve gereksinim analizi
2. **Tasarım Aşaması**: Sistem mimarisi ve bileşen tasarımı
3. **Geliştirme Aşaması**: Sistem kodlama ve entegrasyon
4. **Test Aşaması**: Fonksiyonel ve performans testleri
5. **Değerlendirme Aşaması**: Kullanıcı deneyimi ve sistem etkinliği değerlendirmesi

### 3.1.2 Araştırma Yaklaşımı

Bu çalışmada **karma yöntem (Mixed Methods)** yaklaşımı benimsenmiştir. Karma yöntem, nicel ve nitel veri toplama tekniklerini birleştiren bir araştırma yaklaşımıdır (Creswell, 2014).

**Nicel Yöntemler:**
- Sistem performans metrikleri (yanıt süresi, doğruluk oranı)
- Kullanıcı etkileşim istatistikleri
- API performans testleri

**Nitel Yöntemler:**
- Kullanıcı deneyimi anketleri
- Uzman görüşleri
- Sistem kullanılabilirlik değerlendirmesi

### 3.1.3 Veri Toplama Yöntemleri

#### 3.1.3.1 Birincil Veri Kaynakları

**Teknik Veriler:**
- Sistem performans logları
- API yanıt süreleri
- Veritabanı sorgu performansları
- Kullanıcı etkileşim verileri

**Kullanıcı Verileri:**
- Anket formları
- Görüşme kayıtları
- Kullanıcı geri bildirimleri
- Sistem kullanım istatistikleri

#### 3.1.3.2 İkincil Veri Kaynakları

**Akademik Kaynaklar:**
- Bilimsel makaleler
- Tez çalışmaları
- Konferans bildirileri
- Teknik raporlar

**Teknik Dokümantasyon:**
- API dokümantasyonları
- Framework kılavuzları
- Teknoloji rehberleri
- Açık kaynak proje dokümantasyonları

## 3.2 Kullanılan Teknolojiler

### 3.2.1 Teknoloji Seçim Kriterleri

Teknoloji seçiminde aşağıdaki kriterler dikkate alınmıştır:

1. **Performans**: Yüksek performans ve hızlı yanıt süreleri
2. **Ölçeklenebilirlik**: Artan kullanıcı sayısına uyum sağlama
3. **Güvenilirlik**: Kararlı ve güvenilir çalışma
4. **Geliştirilebilirlik**: Kolay bakım ve güncelleme
5. **Maliyet Etkinliği**: Açık kaynak ve ücretsiz alternatifler
6. **Topluluk Desteği**: Aktif geliştirici topluluğu
7. **Dokümantasyon**: Kapsamlı ve güncel dokümantasyon

### 3.2.2 Backend Teknolojileri

#### 3.2.2.1 FastAPI

**Seçim Gerekçesi:**
- Modern Python web framework'ü
- Otomatik API dokümantasyonu (Swagger/OpenAPI)
- Yüksek performans (Node.js ve Go ile karşılaştırılabilir)
- Tip güvenliği (Pydantic entegrasyonu)
- Asenkron programlama desteği

**Kullanım Alanları:**
- RESTful API geliştirme
- Kullanıcı kimlik doğrulama
- Chat endpoint'leri
- Admin panel API'leri

#### 3.2.2.2 SQLAlchemy

**Seçim Gerekçesi:**
- Python için en popüler ORM (Object-Relational Mapping)
- Çoklu veritabanı desteği
- Güçlü sorgu API'si
- Migrasyon desteği (Alembic)
- Performans optimizasyonları

**Kullanım Alanları:**
- Kullanıcı veritabanı yönetimi
- Konuşma geçmişi saklama
- Hayvancılık bilgi tabanı
- Sistem logları

#### 3.2.2.3 Python

**Seçim Gerekçesi:**
- Yapay zeka ve makine öğrenmesi için en uygun dil
- Zengin kütüphane ekosistemi
- Kolay öğrenme eğrisi
- Açık kaynak ve ücretsiz
- Büyük geliştirici topluluğu

### 3.2.3 Yapay Zeka ve NLP Teknolojileri

#### 3.2.3.1 LangChain

**Seçim Gerekçesi:**
- RAG sistemleri için özel olarak tasarlanmış
- Modüler ve genişletilebilir yapı
- Çoklu LLM desteği
- Vektör veritabanı entegrasyonu
- Prompt yönetimi araçları

**Kullanım Alanları:**
- RAG sistemi geliştirme
- Belge işleme ve parçalama
- Embedding oluşturma
- LLM entegrasyonu

#### 3.2.3.2 OpenAI GPT

**Seçim Gerekçesi:**
- En gelişmiş büyük dil modelleri
- Türkçe dil desteği
- Yüksek doğruluk oranı
- API tabanlı erişim
- Sürekli güncellemeler

**Kullanım Alanları:**
- Doğal dil anlama
- Metin üretimi
- Soru-cevap sistemleri
- İçerik özetleme

#### 3.2.3.3 ChromaDB

**Seçim Gerekçesi:**
- Açık kaynak vektör veritabanı
- Python entegrasyonu
- Yüksek performans
- Kolay kurulum ve kullanım
- Embedding optimizasyonu

**Kullanım Alanları:**
- Vektör depolama
- Benzerlik araması
- Embedding yönetimi
- RAG sistemi desteği

#### 3.2.3.4 Sentence Transformers

**Seçim Gerekçesi:**
- Türkçe dil modelleri desteği
- Yüksek kaliteli embedding'ler
- Hızlı işleme
- Açık kaynak
- Kolay entegrasyon

**Kullanım Alanları:**
- Metin embedding oluşturma
- Benzerlik hesaplama
- Belge vektörleştirme

### 3.2.4 Frontend Teknolojileri

#### 3.2.4.1 HTML5, CSS3, JavaScript

**Seçim Gerekçesi:**
- Web standartları
- Tarayıcı uyumluluğu
- Responsive tasarım
- Hızlı geliştirme
- Kolay bakım

**Kullanım Alanları:**
- Kullanıcı arayüzü
- Chat arayüzü
- Admin paneli
- Responsive tasarım

### 3.2.5 Veritabanı Teknolojileri

#### 3.2.5.1 SQLite

**Seçim Gerekçesi:**
- Geliştirme aşamasında kolaylık
- Dosya tabanlı veritabanı
- Sıfır konfigürasyon
- Hızlı prototipleme
- Ücretsiz

**Kullanım Alanları:**
- Geliştirme ortamı
- Prototip testleri
- Küçük ölçekli uygulamalar

#### 3.2.5.2 PostgreSQL (Üretim)

**Seçim Gerekçesi:**
- Güçlü ilişkisel veritabanı
- JSON desteği
- Yüksek performans
- Ölçeklenebilirlik
- Açık kaynak

**Kullanım Alanları:**
- Üretim ortamı
- Büyük veri setleri
- Karmaşık sorgular

## 3.3 Veri Toplama ve Hazırlama

### 3.3.1 Hayvancılık Bilgi Veritabanı Oluşturma

#### 3.3.1.1 Veri Kaynakları

**Akademik Kaynaklar:**
- Tarım ve Orman Bakanlığı yayınları
- Veteriner Hekim Derneği raporları
- Üniversite araştırma makaleleri
- Hayvancılık Araştırma Enstitüsü yayınları

**Uzman Kaynaklar:**
- Veteriner hekim görüşleri
- Hayvancılık uzmanı danışmanlıkları
- Sektör deneyimleri
- Pratik uygulama örnekleri

**Resmi Kaynaklar:**
- Tarım ve Orman Bakanlığı rehberleri
- Hayvancılık Genel Müdürlüğü yayınları
- İl Tarım Müdürlükleri raporları
- Kooperatif bilgi bankaları

#### 3.3.1.2 Veri Kategorileri

**Sığır Yetiştiriciliği:**
- Beslenme programları
- Sağlık ve hastalık yönetimi
- Üretim teknikleri
- Barınak tasarımı
- Ekonomik analiz

**Kümes Hayvanları:**
- Tavuk yetiştiriciliği
- Hindi yetiştiriciliği
- Yumurta üretimi
- Kümes yönetimi
- Sağlık kontrolü

**Koyun ve Keçi:**
- Mer'a yönetimi
- Beslenme programları
- Üreme yönetimi
- Sağlık kontrolü
- Ürün işleme

**Genel Konular:**
- Barınak tasarımı
- Sağlık ve aşılama
- Ekonomik yönetim
- Çevre yönetimi
- Teknoloji kullanımı

#### 3.3.1.3 Veri İşleme Süreci

**1. Veri Toplama:**
- Kaynak belgelerin taranması
- Uzman görüşlerinin alınması
- Mevcut bilgi bankalarının incelenmesi

**2. Veri Temizleme:**
- Gereksiz bilgilerin çıkarılması
- Format standardizasyonu
- Dil tutarlılığının sağlanması

**3. Veri Kategorilendirme:**
- Konu bazında sınıflandırma
- Alt kategorilerin belirlenmesi
- Etiketleme sistemi

**4. Veri Doğrulama:**
- Uzman kontrolü
- Çapraz referans kontrolü
- Güncellik kontrolü

### 3.3.2 Veri Yapısı ve Formatı

#### 3.3.2.1 Veri Modeli

```json
{
  "id": "unique_identifier",
  "category": "sığır|kümes_hayvanları|koyun_keçi|genel",
  "subcategory": "beslenme|sağlık|üretim|barınak|ekonomi",
  "title": "Başlık",
  "content": "Detaylı içerik",
  "source": "Kaynak bilgisi",
  "keywords": ["anahtar", "kelimeler"],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z",
  "expert_verified": true,
  "language": "tr"
}
```

#### 3.3.2.2 Veri Kalite Kriterleri

**Doğruluk:**
- Uzman onayı
- Kaynak doğrulaması
- Güncel bilgi

**Kapsamlılık:**
- Konu bütünlüğü
- Detay seviyesi
- Pratik uygulanabilirlik

**Tutarlılık:**
- Dil standardı
- Format tutarlılığı
- Terminoloji birliği

## 3.4 Sistem Mimarisi

### 3.4.1 Genel Mimari

Sistem, **mikroservis mimarisi** prensiplerine uygun olarak tasarlanmıştır. Bu mimari, aşağıdaki avantajları sağlamaktadır:

- **Modülerlik**: Bileşenlerin bağımsız geliştirilmesi
- **Ölçeklenebilirlik**: Bileşenlerin ayrı ayrı ölçeklendirilmesi
- **Bakım Kolaylığı**: Hata izolasyonu ve kolay güncelleme
- **Teknoloji Çeşitliliği**: Farklı teknolojilerin kullanılması

### 3.4.2 Sistem Bileşenleri

#### 3.4.2.1 API Katmanı (FastAPI)

**Sorumluluklar:**
- HTTP isteklerinin işlenmesi
- Kimlik doğrulama ve yetkilendirme
- Veri validasyonu
- Hata yönetimi
- API dokümantasyonu

**Endpoint'ler:**
- `/auth/*` - Kimlik doğrulama
- `/chat/*` - Sohbet işlemleri
- `/admin/*` - Yönetim işlemleri
- `/api/*` - Genel API işlemleri

#### 3.4.2.2 İş Mantığı Katmanı

**Sorumluluklar:**
- RAG sistemi yönetimi
- Kullanıcı işlemleri
- Veri işleme
- İş kuralları uygulama

**Bileşenler:**
- Chat Service
- User Service
- Knowledge Service
- Analytics Service

#### 3.4.2.3 Veri Katmanı

**Sorumluluklar:**
- Veri saklama
- Veri erişimi
- Veri bütünlüğü
- Performans optimizasyonu

**Bileşenler:**
- SQLAlchemy ORM
- ChromaDB Vector Store
- File Storage
- Cache Layer

#### 3.4.2.4 RAG Sistemi

**Sorumluluklar:**
- Belge işleme
- Embedding oluşturma
- Benzerlik araması
- Yanıt üretimi

**Bileşenler:**
- Document Processor
- Embedding Generator
- Vector Search
- Response Generator

### 3.4.3 Veri Akışı

#### 3.4.3.1 Kullanıcı Sorgusu İşleme

1. **Sorgu Alımı**: Kullanıcıdan gelen sorgu API'ye ulaşır
2. **Ön İşleme**: Sorgu temizlenir ve normalize edilir
3. **Embedding Oluşturma**: Sorgu vektöre dönüştürülür
4. **Benzerlik Araması**: Vektör veritabanında benzer belgeler aranır
5. **İçerik Alma**: İlgili belgeler çıkarılır
6. **Yanıt Üretimi**: LLM ile yanıt oluşturulur
7. **Yanıt Döndürme**: Kullanıcıya yanıt gönderilir

#### 3.4.3.2 Bilgi Güncelleme

1. **Yeni İçerik**: Uzman tarafından yeni bilgi eklenir
2. **Doğrulama**: İçerik uzman tarafından doğrulanır
3. **İşleme**: İçerik parçalara bölünür
4. **Embedding**: Parçalar vektöre dönüştürülür
5. **Saklama**: Vektörler veritabanına kaydedilir
6. **İndeksleme**: Arama için indekslenir

### 3.4.4 Güvenlik Mimarisi

#### 3.4.4.1 Kimlik Doğrulama

**JWT (JSON Web Token):**
- Stateless kimlik doğrulama
- Güvenli token tabanlı erişim
- Oturum yönetimi
- Yetki kontrolü

#### 3.4.4.2 Veri Güvenliği

**Şifreleme:**
- Bcrypt ile şifre hash'leme
- HTTPS ile veri iletimi
- Veritabanı şifreleme

**Erişim Kontrolü:**
- Role-based access control (RBAC)
- API endpoint koruması
- Rate limiting

## 3.5 Geliştirme Ortamı ve Araçları

### 3.5.1 Geliştirme Ortamı

**İşletim Sistemi:** Windows 10/11, Linux Ubuntu
**Python Sürümü:** 3.12.2
**IDE:** Visual Studio Code, PyCharm
**Versiyon Kontrolü:** Git, GitHub

### 3.5.2 Geliştirme Araçları

**Paket Yönetimi:**
- pip (Python Package Installer)
- virtualenv (Sanal ortam)
- requirements.txt (Bağımlılık yönetimi)

**Test Araçları:**
- pytest (Unit testler)
- Postman (API testleri)
- Selenium (UI testleri)

**Dokümantasyon:**
- Swagger/OpenAPI (API dokümantasyonu)
- Sphinx (Kod dokümantasyonu)
- Markdown (Tez dokümantasyonu)

### 3.5.3 Deployment Araçları

**Containerization:**
- Docker (Containerization)
- Docker Compose (Multi-container)

**Cloud Platforms:**
- Railway (Primary deployment)
- Render (Alternative)
- Heroku (Backup)

**Monitoring:**
- Application logs
- Performance metrics
- Error tracking

## 3.6 Veri Analizi Yöntemleri

### 3.6.1 Performans Analizi

**Metrikler:**
- Yanıt süresi (Response Time)
- Throughput (İşlem hacmi)
- Doğruluk oranı (Accuracy)
- Kullanıcı memnuniyeti (User Satisfaction)

**Analiz Yöntemleri:**
- İstatistiksel analiz
- Trend analizi
- Karşılaştırmalı analiz
- Korelasyon analizi

### 3.6.2 Kullanıcı Deneyimi Analizi

**Veri Toplama:**
- Anket formları
- Kullanıcı geri bildirimleri
- Sistem kullanım logları
- A/B test sonuçları

**Değerlendirme Kriterleri:**
- Kullanılabilirlik (Usability)
- Erişilebilirlik (Accessibility)
- Performans (Performance)
- Memnuniyet (Satisfaction)

### 3.6.3 İçerik Analizi

**Kalite Metrikleri:**
- İçerik doğruluğu
- Güncellik
- Kapsamlılık
- Anlaşılabilirlik

**Analiz Yöntemleri:**
- Uzman değerlendirmesi
- Kullanıcı testleri
- Otomatik metrikler
- Karşılaştırmalı analiz

Bu bölümde, araştırmanın yöntemsel temelleri, kullanılan teknolojiler ve sistem mimarisi detaylı olarak açıklanmıştır. Bir sonraki bölümde, sistem tasarımı ve geliştirme süreci ele alınacaktır.

