@echo off
echo ========================================
echo   AKILLI CIFTLIK YONETIM SISTEMI
echo   Otomatik Kurulum Scripti
echo ========================================
echo.

echo [1/6] Python versiyonu kontrol ediliyor...
python --version
if %errorlevel% neq 0 (
    echo HATA: Python yuklu degil! Lutfen Python 3.11+ yukleyin.
    pause
    exit /b 1
)
echo.

echo [2/6] Sanal ortam olusturuluyor...
if exist venv (
    echo Sanal ortam zaten mevcut, siliniyor...
    rmdir /s /q venv
)
python -m venv venv
if %errorlevel% neq 0 (
    echo HATA: Sanal ortam olusturulamadi!
    pause
    exit /b 1
)
echo.

echo [3/6] Sanal ortam aktiflestiriliyor...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo HATA: Sanal ortam aktiflestirilemedi!
    pause
    exit /b 1
)
echo.

echo [4/6] Pip guncelleniyor...
python -m pip install --upgrade pip
echo.

echo [5/6] Gerekli paketler yukleniyor...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo HATA: Paketler yuklenemedi!
    pause
    exit /b 1
)
echo.

echo [6/6] Veritabani hazirlaniyor...
if exist livestock_chatbot.db (
    echo Eski veritabani siliniyor...
    del livestock_chatbot.db
)
echo.

echo ========================================
echo   KURULUM TAMAMLANDI!
echo ========================================
echo.
echo Uygulamayi baslatmak icin:
echo   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
echo.
echo Tarayicida acmak icin:
echo   http://localhost:8000
echo.
echo Varsayilan admin hesabi:
echo   E-posta: admin@livestock.com
echo   Sifre: admin123
echo.
echo ========================================

pause

