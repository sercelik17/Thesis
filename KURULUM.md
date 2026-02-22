# 🚀 Hayvancılık AI Sohbet Robotu - Kurulum Rehberi

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git (opsiyonel)

## 🔧 Kurulum Adımları

### 1. Sanal Ortam Oluşturun
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 3. Ortam Değişkenlerini Ayarlayın
```bash
# env.example dosyasını .env olarak kopyalayın
copy env.example .env

# .env dosyasını düzenleyin ve aşağıdaki değerleri girin:
```

**Önemli**: `.env` dosyasında aşağıdaki değerleri ayarlayın:
```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
```

### 4. Uygulamayı Başlatın

#### Yöntem 1: run.py ile
```bash
python run.py
```

#### Yöntem 2: Modül olarak
```bash
python -m app
```

#### Yöntem 3: Doğrudan
```bash
python -m app.main
```

## 🌐 Erişim Adresleri

Uygulama başladıktan sonra aşağıdaki adreslerden erişebilirsiniz:

- **Kullanıcı Arayüzü**: http://localhost:8000/chat
- **Admin Paneli**: http://localhost:8000/admin
- **API Dokümantasyonu**: http://localhost:8000/docs
- **Ana Sayfa**: http://localhost:8000

## 👤 Varsayılan Admin Hesabı

- **E-posta**: admin@livestock.com
- **Şifre**: admin123

## 🧪 Test Etme

### 1. Kullanıcı Kaydı
1. http://localhost:8000/chat adresine gidin
2. "Kayıt olun" linkine tıklayın
3. Yeni hesap oluşturun

### 2. Sohbet Testi
1. Giriş yapın
2. Hayvancılık konularında sorular sorun:
   - "Sığır beslenmesi hakkında bilgi verir misin?"
   - "Tavuk yetiştiriciliğinde dikkat edilmesi gerekenler nelerdir?"
   - "Koyun sağlığı için hangi aşılar gerekli?"

### 3. Admin Paneli Testi
1. http://localhost:8000/admin adresine gidin
2. Admin hesabıyla giriş yapın
3. Kullanıcıları ve bilgi bankasını yönetin

## 🔧 Sorun Giderme

### Yaygın Hatalar

#### 1. "ModuleNotFoundError"
```bash
# Sanal ortamın aktif olduğundan emin olun
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

#### 2. "OpenAI API Key" Hatası
- `.env` dosyasında `OPENAI_API_KEY` değerini kontrol edin
- OpenAI API key'inizin geçerli olduğundan emin olun

#### 3. "Port already in use" Hatası
```bash
# Farklı port kullanın
python run.py --port 8001
```

#### 4. Veritabanı Hatası
```bash
# Veritabanı dosyasını silin ve yeniden başlatın
del livestock_chatbot.db
python run.py
```

## 📊 Performans İpuçları

### 1. İlk Başlatma
- İlk başlatmada RAG sistemi ve veritabanı hazırlanması biraz zaman alabilir
- ChromaDB vektör veritabanı oluşturulacaktır

### 2. Bellek Kullanımı
- Uygulama yaklaşık 500MB-1GB RAM kullanabilir
- Büyük modeller için daha fazla bellek gerekebilir

### 3. Hız Optimizasyonu
- İlk sorgu biraz yavaş olabilir (model yükleme)
- Sonraki sorgular daha hızlı olacaktır

## 🚀 Üretim Ortamı

### Güvenlik
- `SECRET_KEY` için güçlü bir değer kullanın
- `DEBUG=False` yapın
- HTTPS kullanın

### Performans
- PostgreSQL kullanın (SQLite yerine)
- Redis cache ekleyin
- Load balancer kullanın

### Monitoring
- Log dosyalarını izleyin
- Sistem kaynaklarını monitör edin
- Kullanıcı aktivitelerini takip edin

## 📞 Destek

Sorunlarınız için:
1. README.md dosyasını kontrol edin
2. GitHub Issues'da arama yapın
3. Yeni issue oluşturun

---

**Başarılı kurulum! 🎉**

Artık hayvancılık AI sohbet robotunuz kullanıma hazır!

