#!/usr/bin/env python3
"""
Credential Dumping Test Tool
Bu araç, Windows'ta credential dumping aktivitelerini simüle eder ve AV/EDR tepkisini test eder.

⚠️ UYARI: Bu araç sadece kendi sisteminizde ve yetkili test ortamlarında kullanılmalıdır.
Eğitim ve araştırma amaçlıdır. Zararlı amaçla kullanmayın.
"""

import ctypes
from ctypes import wintypes
import os
import sys
import time
from datetime import datetime

# Windows API tanımlamaları
kernel32 = ctypes.windll.kernel32
advapi32 = ctypes.windll.advapi32
ntdll = ctypes.windll.ntdll

# Sabitler
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
PROCESS_ALL_ACCESS = 0x001F03FF
KEY_READ = 0x20019
HKEY_LOCAL_MACHINE = 0x80000002

def test_lsass_access():
    """Test 1: LSASS Process'ine Erişim Denemesi"""
    print("[*] Test 1: LSASS Process'ine Erişim Denemesi")
    print("    Bu test, LSASS process'ini bulmaya ve erişmeye çalışır.\n")
    
    try:
        # Process listesi al
        TH32CS_SNAPPROCESS = 0x00000002
        h_snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        
        if h_snapshot == -1:
            print("[-] Process snapshot oluşturulamadı")
            return
        
        class PROCESSENTRY32(ctypes.Structure):
            _fields_ = [
                ("dwSize", wintypes.DWORD),
                ("cntUsage", wintypes.DWORD),
                ("th32ProcessID", wintypes.DWORD),
                ("th32DefaultHeapID", ctypes.POINTER(wintypes.ULONG)),
                ("th32ModuleID", wintypes.DWORD),
                ("cntThreads", wintypes.DWORD),
                ("th32ParentProcessID", wintypes.DWORD),
                ("pcPriClassBase", wintypes.LONG),
                ("dwFlags", wintypes.DWORD),
                ("szExeFile", ctypes.c_char * 260)
            ]
        
        pe32 = PROCESSENTRY32()
        pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)
        
        Process32First = kernel32.Process32First
        Process32First.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32)]
        Process32First.restype = wintypes.BOOL
        
        Process32Next = kernel32.Process32Next
        Process32Next.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32)]
        Process32Next.restype = wintypes.BOOL
        
        lsass_pid = None
        if Process32First(h_snapshot, ctypes.byref(pe32)):
            while True:
                process_name = pe32.szExeFile.decode('utf-8', errors='ignore')
                if "lsass.exe" in process_name.lower():
                    lsass_pid = pe32.th32ProcessID
                    print(f"[+] LSASS process bulundu: PID {lsass_pid}")
                    break
                
                if not Process32Next(h_snapshot, ctypes.byref(pe32)):
                    break
        
        kernel32.CloseHandle(h_snapshot)
        
        if lsass_pid:
            # LSASS'e erişmeye çalış (sadece test, gerçek dump yapmıyoruz)
            print(f"[*] LSASS process'ine erişmeye çalışılıyor (PID: {lsass_pid})...")
            
            OpenProcess = kernel32.OpenProcess
            OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            OpenProcess.restype = wintypes.HANDLE
            
            h_process = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, lsass_pid)
            
            if h_process:
                print("[!] LSASS process'ine erişim başarılı (AV/EDR bu aktiviteyi tespit etmeli)")
                print("    Not: Gerçek bellek dump yapılmıyor, sadece erişim test ediliyor")
                
                # Process bilgilerini oku (sadece test)
                try:
                    ReadProcessMemory = kernel32.ReadProcessMemory
                    ReadProcessMemory.argtypes = [
                        wintypes.HANDLE,
                        wintypes.LPVOID,
                        wintypes.LPVOID,
                        ctypes.c_size_t,
                        ctypes.POINTER(ctypes.c_size_t)
                    ]
                    ReadProcessMemory.restype = wintypes.BOOL
                    
                    buffer = (ctypes.c_byte * 4)()
                    bytes_read = ctypes.c_size_t()
                    
                    # Sadece küçük bir okuma denemesi (test amaçlı)
                    result = ReadProcessMemory(
                        h_process,
                        0x1000,  # Rastgele bir adres
                        buffer,
                        4,
                        ctypes.byref(bytes_read)
                    )
                    
                    if result:
                        print("[!] LSASS bellek okuma denemesi yapıldı (AV/EDR tespit etmeli)")
                    else:
                        print("[*] LSASS bellek okuma başarısız (beklenen)")
                except Exception as e:
                    print(f"[*] Bellek okuma testi: {e}")
                
                kernel32.CloseHandle(h_process)
            else:
                error = kernel32.GetLastError()
                print(f"[-] LSASS'e erişim reddedildi (Error: {error})")
                print("    Bu normal olabilir - yönetici hakları veya AV/EDR koruması")
        else:
            print("[-] LSASS process bulunamadı")
            
    except Exception as e:
        print(f"[-] Hata: {e}")
        import traceback
        traceback.print_exc()
    
    print()

def test_registry_sam_access():
    """Test 2: Registry'den SAM Bilgilerine Erişim Denemesi"""
    print("[*] Test 2: Registry'den SAM Bilgilerine Erişim Denemesi")
    print("    Bu test, SAM kayıt defteri anahtarına erişmeye çalışır.\n")
    
    try:
        # SAM registry anahtarına erişmeye çalış
        sam_key_path = r"SYSTEM\CurrentControlSet\Control\Lsa"
        
        RegOpenKeyEx = advapi32.RegOpenKeyExW
        RegOpenKeyEx.argtypes = [
            wintypes.HKEY,
            wintypes.LPCWSTR,
            wintypes.DWORD,
            wintypes.REGSAM,
            ctypes.POINTER(wintypes.HKEY)
        ]
        RegOpenKeyEx.restype = wintypes.LONG
        
        h_key = wintypes.HKEY()
        
        # LSA anahtarına erişmeye çalış
        result = RegOpenKeyEx(
            HKEY_LOCAL_MACHINE,
            sam_key_path,
            0,
            KEY_READ,
            ctypes.byref(h_key)
        )
        
        if result == 0:  # ERROR_SUCCESS
            print("[!] LSA registry anahtarına erişim başarılı (AV/EDR tespit etmeli)")
            
            # Değer okumaya çalış
            RegQueryValueEx = advapi32.RegQueryValueExW
            RegQueryValueEx.argtypes = [
                wintypes.HKEY,
                wintypes.LPCWSTR,
                ctypes.POINTER(wintypes.LPDWORD),
                ctypes.POINTER(wintypes.DWORD),
                ctypes.POINTER(ctypes.c_byte),
                ctypes.POINTER(wintypes.DWORD)
            ]
            RegQueryValueEx.restype = wintypes.LONG
            
            # Sadece anahtar varlığını kontrol et
            print("[*] Registry değerlerini okumaya çalışılıyor...")
            
            RegCloseKey = advapi32.RegCloseKey
            RegCloseKey.argtypes = [wintypes.HKEY]
            RegCloseKey.restype = wintypes.LONG
            RegCloseKey(h_key)
        else:
            print(f"[-] LSA registry anahtarına erişim reddedildi (Error: {result})")
            print("    Bu normal olabilir - yönetici hakları veya AV/EDR koruması")
            
    except Exception as e:
        print(f"[-] Hata: {e}")
        import traceback
        traceback.print_exc()
    
    print()

def test_credential_manager_access():
    """Test 3: Windows Credential Manager Erişimi"""
    print("[*] Test 3: Windows Credential Manager Erişimi")
    print("    Bu test, Credential Manager API'lerini çağırır.\n")
    
    try:
        # CredUI API'lerini yükle
        try:
            credapi = ctypes.windll.credui
        except:
            print("[-] CredUI.dll yüklenemedi")
            return
        
        # CredEnumerate API'sini çağırmaya çalış
        # Bu, kayıtlı kimlik bilgilerini listeler
        print("[*] CredEnumerate API'sini çağırmaya çalışılıyor...")
        print("    Not: Bu API çağrısı AV/EDR tarafından izlenebilir")
        
        # CredEnumerate tanımı
        CredEnumerate = advapi32.CredEnumerateW
        CredEnumerate.argtypes = [
            wintypes.LPCWSTR,  # Filter
            ctypes.c_uint,     # Flags
            ctypes.POINTER(ctypes.c_uint),  # Count
            ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))  # Credentials
        ]
        CredEnumerate.restype = wintypes.BOOL
        
        count = ctypes.c_uint()
        credentials = ctypes.POINTER(ctypes.c_void_p)()
        
        # Tüm kimlik bilgilerini listele
        result = CredEnumerate(None, 0, ctypes.byref(count), ctypes.byref(credentials))
        
        if result:
            print(f"[!] CredEnumerate başarılı: {count.value} kimlik bilgisi bulundu")
            print("    AV/EDR bu aktiviteyi tespit etmeli")
            
            # CredFree ile temizle
            CredFree = advapi32.CredFree
            CredFree.argtypes = [ctypes.c_void_p]
            CredFree.restype = None
            CredFree(credentials)
        else:
            error = kernel32.GetLastError()
            print(f"[-] CredEnumerate başarısız (Error: {error})")
            
    except Exception as e:
        print(f"[-] Hata: {e}")
        import traceback
        traceback.print_exc()
    
    print()

def test_security_descriptor_access():
    """Test 4: Güvenlik Tanımlayıcılarına Erişim"""
    print("[*] Test 4: Güvenlik Tanımlayıcılarına Erişim")
    print("    Bu test, sistem güvenlik tanımlayıcılarına erişmeye çalışır.\n")
    
    try:
        # GetTokenInformation API'sini kullan
        # Bu, process token bilgilerini okur
        print("[*] Process token bilgilerini okumaya çalışılıyor...")
        
        # Mevcut process handle'ı al
        current_process = kernel32.GetCurrentProcess()
        
        OpenProcessToken = advapi32.OpenProcessToken
        OpenProcessToken.argtypes = [
            wintypes.HANDLE,
            wintypes.DWORD,
            ctypes.POINTER(wintypes.HANDLE)
        ]
        OpenProcessToken.restype = wintypes.BOOL
        
        TOKEN_QUERY = 0x0008
        h_token = wintypes.HANDLE()
        
        if OpenProcessToken(current_process, TOKEN_QUERY, ctypes.byref(h_token)):
            print("[!] Process token'a erişim başarılı")
            print("    Token bilgileri okunabilir (AV/EDR tespit etmeli)")
            
            # Token bilgilerini oku
            GetTokenInformation = advapi32.GetTokenInformation
            GetTokenInformation.argtypes = [
                wintypes.HANDLE,
                ctypes.c_uint,  # TokenInformationClass
                ctypes.c_void_p,
                wintypes.DWORD,
                ctypes.POINTER(wintypes.DWORD)
            ]
            GetTokenInformation.restype = wintypes.BOOL
            
            # Token user bilgilerini al
            TOKEN_INFORMATION_CLASS = 1  # TokenUser
            buffer_size = wintypes.DWORD()
            
            GetTokenInformation(h_token, TOKEN_INFORMATION_CLASS, None, 0, ctypes.byref(buffer_size))
            
            if buffer_size.value > 0:
                buffer = (ctypes.c_byte * buffer_size.value)()
                if GetTokenInformation(h_token, TOKEN_INFORMATION_CLASS, buffer, buffer_size.value, ctypes.byref(buffer_size)):
                    print("[!] Token bilgileri okundu (AV/EDR tespit etmeli)")
            
            CloseHandle = kernel32.CloseHandle
            CloseHandle(h_token)
        else:
            error = kernel32.GetLastError()
            print(f"[-] Process token'a erişim reddedildi (Error: {error})")
            
    except Exception as e:
        print(f"[-] Hata: {e}")
        import traceback
        traceback.print_exc()
    
    print()

def save_test_results(filename):
    """Test sonuçlarını dosyaya kaydet"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Credential Dumping Test Sonuçları\n")
            f.write("==================================\n\n")
            f.write(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Python Sürümü: {sys.version}\n")
            f.write(f"İşletim Sistemi: {os.name}\n")
            f.write("\n")
            f.write("Test Senaryoları:\n")
            f.write("1. LSASS Process Erişimi\n")
            f.write("2. Registry SAM Erişimi\n")
            f.write("3. Credential Manager Erişimi\n")
            f.write("4. Security Descriptor Erişimi\n")
            f.write("\n")
            f.write("⚠️ UYARI: Bu test sadece eğitim ve araştırma amaçlıdır.\n")
            f.write("Sadece kendi sisteminizde ve yetkili test ortamlarında kullanın.\n")
            f.write("\n")
            f.write("AV/EDR Tepkisini Kontrol Edin:\n")
            f.write("- Chomar Internet Security logları\n")
            f.write("- Windows Event Viewer (Security logs)\n")
            f.write("- Process Monitor ile syscall'ları izleyin\n")
        
        print(f"[+] Test sonuçları kaydedildi: {filename}")
    except Exception as e:
        print(f"[-] Test sonuçları kaydedilemedi: {e}")

def main():
    print("=" * 70)
    print("Credential Dumping Test Tool")
    print("=" * 70)
    print()
    print("⚠️ UYARI: Bu araç sadece kendi sisteminizde ve yetkili test ortamlarında kullanılmalıdır.")
    print("⚠️ Eğitim ve araştırma amaçlıdır. Zararlı amaçla kullanmayın.")
    print("⚠️ Bu testler AV/EDR tarafından tespit edilebilir.")
    print()
    
    # Yönetici hakları kontrolü
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("[!] UYARI: Yönetici hakları yok. Bazı testler başarısız olabilir.")
            print("    Testleri yönetici olarak çalıştırmanız önerilir.")
            print()
    except:
        pass
    
    input("Devam etmek için Enter'a basın...")
    print()
    
    # Testleri çalıştır
    test_lsass_access()
    time.sleep(2)  # AV'nin tepkisini gözlemlemek için bekle
    
    test_registry_sam_access()
    time.sleep(2)
    
    test_credential_manager_access()
    time.sleep(2)
    
    test_security_descriptor_access()
    
    # Sonuçları kaydet
    save_test_results("credential_dumping_test_results.txt")
    
    print()
    print("=" * 70)
    print("Test tamamlandı!")
    print("=" * 70)
    print()
    print("Sonraki adımlar:")
    print("1. Chomar Internet Security loglarını kontrol edin")
    print("2. Event Viewer'da güvenlik olaylarını inceleyin (Windows Logs > Security)")
    print("3. Test sonuçlarını credential_dumping_test_results.txt dosyasından okuyun")
    print()
    print("AV/EDR Tepkisini Gözlemleme:")
    print("- Chomar: Loglar/Geçmiş bölümü")
    print("- Event Viewer: Security logs, 'LSASS', 'Credential', 'SAM' kelimelerini arayın")
    print("- Process Monitor: LSASS process'ine yapılan erişimleri izleyin")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Test kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n[-] Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()
