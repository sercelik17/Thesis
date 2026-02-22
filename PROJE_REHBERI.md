# 🏡 Akıllı Çiftlik Yönetim Sistemi - Proje Rehberi

## 📋 Proje Özeti

Bu proje, yapay zeka destekli akıllı çiftlik yönetim sistemidir. RAG (Retrieval-Augmented Generation) teknolojisi kullanarak çiftlik sahiplerinin doğal dilde sorular sorabilmesini ve akıllı öneriler alabilmesini sağlar.

### 🎯 Ana Özellikler

- **🔐 Güvenli Giriş Sistemi**: JWT tabanlı authentication
- **🐄 Hayvan Yönetimi**: Hayvan kayıtları, sağlık takibi, üretim performansı
- **📊 Analitik Dashboard**: Gerçek zamanlı çiftlik analizi
- **🤖 AI Asistan**: Doğal dil ile çiftlik verilerini sorgulama
- **💰 Finansal Yönetim**: Gelir-gider takibi ve karlılık analizi
- **🌾 Yem Yönetimi**: Yem tüketimi ve maliyet optimizasyonu
- **📱 Responsive Tasarım**: Mobil ve masaüstü uyumlu arayüz

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.11+
- Git
- Modern web tarayıcısı

### 1. Projeyi İndirin

```bash
git clone [repository-url]
cd TEZ
```

### 2. Sanal Ortam Oluşturun

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Uygulamayı Başlatın

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Tarayıcıda Açın

```
http://localhost:8000
```

## 🔧 Detaylı Kurulum

### Adım 1: Python Kurulumu

Python 3.11 veya üzeri sürümün yüklü olduğundan emin olun:

```bash
python --version
```

### Adım 2: Proje Dosyalarını İndirin

Proje dosyalarını bilgisayarınıza indirin ve bir klasöre çıkarın.

### Adım 3: Sanal Ortam Kurulumu

```bash
# Proje klasörüne gidin
cd TEZ

# Sanal ortam oluşturun
python -m venv venv

# Sanal ortamı aktifleştirin
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### Adım 4: Bağımlılık Yükleme

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Adım 5: Veritabanı Başlatma

Uygulama ilk çalıştırıldığında otomatik olarak SQLite veritabanı oluşturulur.

### Adım 6: Uygulamayı Başlatma

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Başarılı kurulum sonrası şu mesajı göreceksiniz:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 🌐 Kullanım Rehberi

### 1. Ana Sayfa

`http://localhost:8000` adresine gidin. Ana sayfada şu seçenekleri göreceksiniz:

- **🔐 Giriş Yap**: Mevcut kullanıcı girişi
- **📝 Kayıt Ol**: Yeni kullanıcı kaydı
- **🚀 Çiftlik Yönetimi**: Çiftlik arayüzü (giriş gerekli)
- **📚 API Dokümantasyonu**: Swagger UI

### 2. Kullanıcı Kaydı

1. "📝 Kayıt Ol" butonuna tıklayın
2. Gerekli bilgileri doldurun:
   - E-posta
   - Kullanıcı adı
   - Ad Soyad
   - Şifre
3. "Kayıt Ol" butonuna tıklayın

### 3. Giriş Yapma

1. "🔐 Giriş Yap" butonuna tıklayın
2. E-posta ve şifrenizi girin
3. "Giriş Yap" butonuna tıklayın

**Varsayılan Admin Hesabı:**
- E-posta: `admin@livestock.com`
- Şifre: `admin123`

### 4. Çiftlik Oluşturma

Giriş yaptıktan sonra:

1. "🚀 Çiftlik Yönetimi" sayfasına gidin
2. "Yeni Çiftlik Oluştur" butonuna tıklayın
3. Çiftlik bilgilerini doldurun:
   - Çiftlik adı
   - Konum
   - Çiftlik türü
   - Toplam alan
4. "Çiftlik Oluştur" butonuna tıklayın

### 5. Hayvan Ekleme

1. Çiftlik seçin
2. "Hayvan Yönetimi" sekmesine gidin
3. "Yeni Hayvan Ekle" butonuna tıklayın
4. Hayvan bilgilerini doldurun:
   - Küpe numarası
   - Ad
   - Tür
   - Irk
   - Cinsiyet
   - Doğum tarihi
   - Ağırlık
5. "Hayvan Ekle" butonuna tıklayın

### 6. AI Asistan Kullanımı

1. Çiftlik seçin
2. "AI Asistan" sekmesine gidin
3. Doğal dilde sorularınızı yazın:

**Örnek Sorular:**
- "Bu ay ne kadar süt üretimi yaptım?"
- "Hangi hayvanların aşı zamanı geldi?"
- "Çiftliğimdeki karlılık oranı nedir?"
- "Yem maliyetlerimi nasıl optimize edebilirim?"
- "Hangi hayvanların sağlık durumu kritik?"

### 7. Analitik Dashboard

1. Çiftlik seçin
2. "Dashboard" sekmesine gidin
3. Gerçek zamanlı analizleri görün:
   - Toplam hayvan sayısı
   - Aylık üretim
   - Sağlık durumu
   - Finansal özet

## 🧪 Test Senaryoları

### 1. Temel Fonksiyon Testi

```bash
# Test scriptlerini çalıştırın
python test_app.py
python test_farm_creation.py
python test_analytics.py
python test_chat.py
```

### 2. Güvenlik Testi

```bash
python test_security.py
python test_unauthorized_access.py
```

### 3. Manuel Test Senaryoları

1. **Kullanıcı Kaydı ve Girişi**
   - Yeni kullanıcı kaydı
   - Giriş yapma
   - Çıkış yapma

2. **Çiftlik Yönetimi**
   - Çiftlik oluşturma
   - Çiftlik bilgilerini güncelleme
   - Çiftlik silme

3. **Hayvan Yönetimi**
   - Hayvan ekleme
   - Hayvan bilgilerini güncelleme
   - Hayvan silme

4. **Veri Girişi**
   - Üretim kayıtları
   - Finansal kayıtlar
   - Sağlık kayıtları
   - Yem kayıtları

5. **AI Asistan**
   - Doğal dil sorguları
   - Analitik sorular
   - Öneri alma

## 🔍 API Dokümantasyonu

Uygulama çalışırken API dokümantasyonuna erişmek için:

```
http://localhost:8000/docs
```

Bu sayfada tüm API endpoint'lerini test edebilirsiniz.

## 🐛 Sorun Giderme

### Yaygın Sorunlar

1. **Port 8000 Kullanımda**
   ```bash
   # Farklı port kullanın
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
   ```

2. **Bağımlılık Hatası**
   ```bash
   # Sanal ortamı yeniden oluşturun
   deactivate
   rmdir /s venv
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Veritabanı Hatası**
   ```bash
   # Veritabanını silin (yeniden oluşturulacak)
   del livestock_chatbot.db
   ```

4. **Import Hatası**
   ```bash
   # Python path'ini kontrol edin
   python -c "import sys; print(sys.path)"
   ```

### Log Kontrolü

Uygulama çalışırken terminal çıktısını kontrol edin. Hata mesajları burada görünecektir.

## 📊 Sistem Gereksinimleri

### Minimum Gereksinimler
- **İşletim Sistemi**: Windows 10, macOS 10.14, Ubuntu 18.04
- **RAM**: 4 GB
- **Disk Alanı**: 2 GB
- **Python**: 3.11+

### Önerilen Gereksinimler
- **RAM**: 8 GB
- **Disk Alanı**: 5 GB
- **İnternet Bağlantısı**: AI özellikleri için

## 🔒 Güvenlik Notları

- Sistem JWT tabanlı güvenlik kullanır
- Şifreler bcrypt ile hash'lenir
- API endpoint'leri authentication gerektirir
- CORS ayarları yapılandırılmıştır

## 📞 Destek

Sorun yaşarsanız:

1. Bu rehberi tekrar okuyun
2. Terminal çıktısını kontrol edin
3. Test scriptlerini çalıştırın
4. API dokümantasyonunu inceleyin

## 🎯 Proje Özellikleri

### Teknik Özellikler
- **Backend**: FastAPI (Python)
- **Veritabanı**: SQLite (geliştirme), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: RAG teknolojisi, Sentence Transformers
- **Güvenlik**: JWT, bcrypt
- **Deployment**: Railway Cloud

### Fonksiyonel Özellikler
- Kullanıcı yönetimi
- Çiftlik yönetimi
- Hayvan takibi
- Üretim analizi
- Finansal yönetim
- Sağlık kayıtları
- Yem yönetimi
- AI asistan
- Gerçek zamanlı dashboard
- Raporlama

## 📈 Performans

- **API Yanıt Süresi**: < 200ms
- **Eşzamanlı Kullanıcı**: 100+
- **Veritabanı Boyutu**: 1GB'a kadar
- **AI Yanıt Süresi**: < 3 saniye

Bu rehber, projeyi başarıyla çalıştırmanız için gerekli tüm bilgileri içermektedir. Herhangi bir sorun yaşarsanız, lütfen terminal çıktısını kontrol edin ve bu rehberdeki adımları takip edin.

