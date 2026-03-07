# Uygulamayı Sürekli Ayakta Tutma (Hoca Kontrolü İçin)

Bilgisayarınız kapalıyken de uygulamanın erişilebilir olması için **Render.com** üzerinde ücretsiz yayına almanız yeterli. Böylece hocanız verdiğiniz linke tıklayarak projeyi inceleyebilir.

---

## 1. Render.com’a Deploy (Ücretsiz)

### Adım 1: GitHub’a push
- Projeyi GitHub’a pushladığınızdan emin olun (`git push origin main` veya ilgili branch).

### Adım 2: Render’da hesap ve servis
1. [https://render.com](https://render.com) → **Get Started** (GitHub ile giriş yapın).
2. **Dashboard** → **New +** → **Web Service**.
3. **Connect a repository** kısmında GitHub repo’nuzu seçin (örn. `sercelik17/Thesis`). İlk seferde “Connect GitHub” deyip yetki verin.
4. Aşağıdaki ayarları girin:

| Ayar | Değer |
|------|--------|
| **Name** | `akilli-ciftlik` (veya istediğiniz isim) |
| **Region** | Frankfurt (veya size yakın) |
| **Branch** | `main` |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

5. **Advanced** → **Environment Variables** kısmına şunları ekleyin:

| Key | Value |
|-----|--------|
| `SECRET_KEY` | Uzun rastgele bir string (örn. `my-super-secret-key-12345`) |
| `ADMIN_EMAIL` | `admin@livestock.com` |
| `ADMIN_PASSWORD` | Girişte kullanılacak admin şifresi (güçlü bir şifre seçin) |

6. **Create Web Service** deyin. İlk deploy 5–10 dakika sürebilir (bağımlılıklar kurulur).

### Adım 3: URL’i alın
- Deploy bittikten sonra üstte **URL** çıkar (örn. `https://akilli-ciftlik-xxxx.onrender.com`).
- Bu linki hocanıza verin. Bilgisayarınız kapalı olsa bile bu adres açık kalır.

---

## 2. Önemli Notlar

- **Ücretsiz plan:** Yaklaşık 15 dakika kimse girmeyince servis “uyur”; ilk istekte 30–60 saniye içinde uyanır. Hocanız linke tıkladığında sayfa biraz gecikmeyle açılır, bu normaldir.
- **Veritabanı:** Ücretsiz planda SQLite kullanılıyor; sunucu yeniden başlarsa veriler sıfırlanabilir. Sadece demo için yeterlidir. Kalıcı veri isterseniz Render’da ücretli PostgreSQL ekleyip `DATABASE_URL` ile bağlayabilirsiniz.
- **Giriş:** Hocanız ana sayfadan **Giriş Yap** → `ADMIN_EMAIL` / `ADMIN_PASSWORD` ile giriş yapıp **Çiftlik Yönetimi** sayfasına gidebilir.

---

## 3. Alternatif: Railway / PythonAnywhere

- **Railway:** [railway.app](https://railway.app) — GitHub bağlayıp benzer şekilde “Deploy” edebilirsiniz; Start Command aynı kalır.
- **PythonAnywhere:** [pythonanywhere.com](https://www.pythonanywhere.com) — Ücretsiz hesapta “Web” oluşturup uygulamayı orada çalıştırabilirsiniz; yapılandırma farklı olduğu için ayrı dokümantasyon gerekir.

Özet: Hocanın sürekli erişebilmesi için **Render’da Web Service oluşturup** yukarıdaki Build/Start komutları ve environment variable’ları kullanmanız yeterli; bilgisayarınız kapalı olsa da uygulama bu URL üzerinden ayakta kalır.
