@echo off
REM User-Mode Syscall Test Tool - Build Script
REM Bu script, C++ test aracını derler

echo ========================================
echo User-Mode Syscall Test Tool - Build
echo ========================================
echo.

REM MinGW veya Visual Studio derleyicisi kontrolü
where g++ >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [*] MinGW g++ bulundu, derleme başlatılıyor...
    g++ -o test_user_mode_syscall.exe test_user_mode_syscall.cpp -static-libgcc -static-libstdc++
    if %ERRORLEVEL% EQU 0 (
        echo [+] Derleme başarılı: test_user_mode_syscall.exe
    ) else (
        echo [-] Derleme başarısız!
        exit /b 1
    )
) else (
    where cl >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo [*] Visual Studio cl.exe bulundu, derleme başlatılıyor...
        cl /EHsc test_user_mode_syscall.cpp /Fe:test_user_mode_syscall.exe
        if %ERRORLEVEL% EQU 0 (
            echo [+] Derleme başarılı: test_user_mode_syscall.exe
        ) else (
            echo [-] Derleme başarısız!
            exit /b 1
        )
    ) else (
        echo [-] Derleyici bulunamadı!
        echo.
        echo Lütfen aşağıdakilerden birini yükleyin:
        echo 1. MinGW-w64 (g++)
        echo 2. Visual Studio (cl.exe)
        echo.
        echo VEYA Python versiyonunu kullanın:
        echo    python test_user_mode_syscall.py
        exit /b 1
    )
)

echo.
echo ========================================
echo Derleme tamamlandı!
echo ========================================
echo.
echo Çalıştırmak için:
echo    test_user_mode_syscall.exe
echo.
pause

