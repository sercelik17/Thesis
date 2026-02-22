@echo off
echo ========================================
echo   HOCA ICIN PROJE PAKETI OLUSTURULUYOR
echo ========================================
echo.

echo [1/4] Gereksiz dosyalar temizleniyor...
if exist __pycache__ rmdir /s /q __pycache__
if exist app\__pycache__ rmdir /s /q app\__pycache__
if exist app\routers\__pycache__ rmdir /s /q app\routers\__pycache__
if exist venv rmdir /s /q venv
if exist livestock_chatbot.db del livestock_chatbot.db
echo.

echo [2/4] Hoca icin ozel dosyalar olusturuluyor...
echo # HOCA ICIN OZEL NOTLAR > HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Proje Hakkinda >> HOCA_NOTLARI.md
echo Bu proje, yapay zeka destekli akilli ciftlik yonetim sistemidir. >> HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Hizli Baslangic >> HOCA_NOTLARI.md
echo 1. KURULUM_SCRIPTI.bat dosyasini calistirin >> HOCA_NOTLARI.md
echo 2. python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload >> HOCA_NOTLARI.md
echo 3. http://localhost:8000 adresini acin >> HOCA_NOTLARI.md
echo 4. admin@livestock.com / admin123 ile giris yapin >> HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Demo >> HOCA_NOTLARI.md
echo python DEMO_SCRIPTI.py >> HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Tez Dokumanlari >> HOCA_NOTLARI.md
echo TEZ/ klasorunde markdown formatinda hazirlanmistir. >> HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Canli Sistem >> HOCA_NOTLARI.md
echo https://haytek.org.tr >> HOCA_NOTLARI.md
echo. >> HOCA_NOTLARI.md
echo ## Iletisim >> HOCA_NOTLARI.md
echo [Ogrenci Adi] - [E-posta] >> HOCA_NOTLARI.md
echo.

echo [3/4] ZIP dosyasi olusturuluyor...
powershell -command "Compress-Archive -Path 'app','static','TEZ','*.py','*.md','*.txt','*.json','*.bat' -DestinationPath 'AKILLI_CIFTLIK_PROJESI.zip' -Force"
echo.

echo [4/4] Paket hazirlaniyor...
echo. > PAKET_ICERIGI.txt
echo AKILLI CIFTLIK YONETIM SISTEMI - HOCA ICIN PAKET >> PAKET_ICERIGI.txt
echo ================================================ >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo PAKET ICERIGI: >> PAKET_ICERIGI.txt
echo - app/ (Ana uygulama kodu) >> PAKET_ICERIGI.txt
echo - static/ (Web arayuzu) >> PAKET_ICERIGI.txt
echo - TEZ/ (Tez dokumanlari) >> PAKET_ICERIGI.txt
echo - requirements.txt (Python bagimliliklari) >> PAKET_ICERIGI.txt
echo - KURULUM_SCRIPTI.bat (Otomatik kurulum) >> PAKET_ICERIGI.txt
echo - DEMO_SCRIPTI.py (Demo scripti) >> PAKET_ICERIGI.txt
echo - HOCA_ICIN_README.md (Detayli rehber) >> PAKET_ICERIGI.txt
echo - PROJE_REHBERI.md (Genel rehber) >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo KURULUM: >> PAKET_ICERIGI.txt
echo 1. KURULUM_SCRIPTI.bat calistirin >> PAKET_ICERIGI.txt
echo 2. python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload >> PAKET_ICERIGI.txt
echo 3. http://localhost:8000 acin >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo DEMO: >> PAKET_ICERIGI.txt
echo python DEMO_SCRIPTI.py >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo CANLI SISTEM: >> PAKET_ICERIGI.txt
echo https://haytek.org.tr >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo TEZ: >> PAKET_ICERIGI.txt
echo TEZ/ klasorunde markdown formatinda >> PAKET_ICERIGI.txt
echo. >> PAKET_ICERIGI.txt
echo ILETISIM: >> PAKET_ICERIGI.txt
echo [Ogrenci Adi] - [E-posta] >> PAKET_ICERIGI.txt
echo.

echo ========================================
echo   PAKET HAZIR!
echo ========================================
echo.
echo Olusturulan dosyalar:
echo - AKILLI_CIFTLIK_PROJESI.zip (Ana paket)
echo - PAKET_ICERIGI.txt (Paket icerigi)
echo - HOCA_NOTLARI.md (Hoca icin notlar)
echo.
echo Hocaya gonderebileceginiz dosyalar:
echo 1. AKILLI_CIFTLIK_PROJESI.zip
echo 2. HOCA_ICIN_README.md
echo 3. PAKET_ICERIGI.txt
echo.
echo ========================================

pause

