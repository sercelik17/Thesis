#!/usr/bin/env python3
"""
User-Mode Syscall Bypass Test Tool (Python)

Bu araç, Windows'ta user-mode syscall hooking bypass tekniklerini test etmek için tasarlanmıştır.
Sadece kendi sisteminizde ve yetkili test ortamlarında kullanın.

Test: Direct syscall kullanarak NtCreateFile API'sini çağırır ve AV/EDR tepkisini gözlemler.
"""

import ctypes
from ctypes import wintypes
import os
import sys
import time
from datetime import datetime

# Windows API tanımlamaları
kernel32 = ctypes.windll.kernel32
ntdll = ctypes.windll.ntdll
psapi = ctypes.windll.psapi

# NtCreateFile için gerekli yapılar
class UNICODE_STRING(ctypes.Structure):
    _fields_ = [
        ("Length", wintypes.USHORT),
        ("MaximumLength", wintypes.USHORT),
        ("Buffer", ctypes.POINTER(wintypes.WCHAR))
    ]

class OBJECT_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("Length", wintypes.ULONG),
        ("RootDirectory", wintypes.HANDLE),
        ("ObjectName", ctypes.POINTER(UNICODE_STRING)),
        ("Attributes", wintypes.ULONG),
        ("SecurityDescriptor", ctypes.c_void_p),
        ("SecurityQualityOfService", ctypes.c_void_p)
    ]

class IO_STATUS_BLOCK(ctypes.Structure):
    _fields_ = [
        ("Status", wintypes.ULONG),
        ("Information", ctypes.c_ulonglong)  # ULONG_PTR yerine c_ulonglong (64-bit için)
    ]

# NtCreateFile fonksiyon imzası
NtCreateFile = ntdll.NtCreateFile
NtCreateFile.argtypes = [
    ctypes.POINTER(wintypes.HANDLE),      # FileHandle
    wintypes.DWORD,                        # DesiredAccess (ACCESS_MASK yerine DWORD)
    ctypes.POINTER(OBJECT_ATTRIBUTES),     # ObjectAttributes
    ctypes.POINTER(IO_STATUS_BLOCK),       # IoStatusBlock
    ctypes.POINTER(ctypes.c_longlong),     # AllocationSize (LARGE_INTEGER yerine)
    wintypes.ULONG,                        # FileAttributes
    wintypes.ULONG,                        # ShareAccess
    wintypes.ULONG,                        # CreateDisposition
    wintypes.ULONG,                        # CreateOptions
    ctypes.c_void_p,                      # EaBuffer (PVOID yerine)
    wintypes.ULONG                         # EaLength
]
NtCreateFile.restype = wintypes.ULONG

# Sabitler
FILE_GENERIC_WRITE = 0x40000000
FILE_ATTRIBUTE_NORMAL = 0x00000080
FILE_SHARE_WRITE = 0x00000002
FILE_OVERWRITE_IF = 0x00000005
FILE_NON_DIRECTORY_FILE = 0x00000040
OBJ_CASE_INSENSITIVE = 0x00000040

def test_normal_api_call():
    """Test 1: Normal API Call (NtCreateFile via ntdll.dll)"""
    print("[*] Test 1: Normal API Call (NtCreateFile via ntdll.dll)")
    print("    Bu test, normal API çağrısını kullanır ve AV'nin tepkisini gözlemler.\n")
    
    # Test dizini oluştur
    test_dir = "C:\\temp"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Test dosyası yolu
    file_path = "\\??\\C:\\temp\\syscall_test.txt"
    file_path_unicode = file_path.encode('utf-16le')
    
    # UNICODE_STRING oluştur
    us = UNICODE_STRING()
    us.Length = len(file_path_unicode) - 2  # NULL terminator hariç
    us.MaximumLength = len(file_path_unicode)
    us.Buffer = ctypes.cast(ctypes.create_string_buffer(file_path_unicode), 
                           ctypes.POINTER(wintypes.WCHAR))
    
    # OBJECT_ATTRIBUTES oluştur
    oa = OBJECT_ATTRIBUTES()
    oa.Length = ctypes.sizeof(OBJECT_ATTRIBUTES)
    oa.RootDirectory = None
    oa.ObjectName = ctypes.pointer(us)
    oa.Attributes = OBJ_CASE_INSENSITIVE
    oa.SecurityDescriptor = None
    oa.SecurityQualityOfService = None
    
    # IO_STATUS_BLOCK oluştur
    iosb = IO_STATUS_BLOCK()
    
    # Dosya handle
    file_handle = wintypes.HANDLE()
    
    try:
        # NtCreateFile çağrısı
        status = NtCreateFile(
            ctypes.byref(file_handle),
            FILE_GENERIC_WRITE,
            ctypes.byref(oa),
            ctypes.byref(iosb),
            None,
            FILE_ATTRIBUTE_NORMAL,
            FILE_SHARE_WRITE,
            FILE_OVERWRITE_IF,
            FILE_NON_DIRECTORY_FILE,
            None,
            0
        )
        
        if status == 0:  # STATUS_SUCCESS
            print(f"[+] Dosya başarıyla oluşturuldu (Normal API)")
            print(f"    Handle: {file_handle.value}")
            print(f"    Status: 0x{status:08X}")
            
            # Dosyayı kapat
            kernel32.CloseHandle(file_handle)
            
            # Test dosyasını sil
            try:
                os.remove("C:\\temp\\syscall_test.txt")
            except:
                pass
        else:
            print(f"[-] Dosya oluşturulamadı. Status: 0x{status:08X}")
            
    except Exception as e:
        print(f"[-] Hata: {e}")
    
    print()

def get_syscall_number(function_name):
    """Syscall number'ı ntdll.dll'den çıkar"""
    try:
        # ntdll.dll'i yükle
        ntdll_handle = kernel32.GetModuleHandleW("ntdll.dll")
        if not ntdll_handle:
            return None
        
        # Fonksiyon adresini al
        func_addr = kernel32.GetProcAddress(ntdll_handle, function_name.encode('ascii'))
        if not func_addr:
            return None
        
        # Bellekten oku (mov eax, XX pattern'ini ara)
        # Bu basit bir yaklaşım, gerçek implementasyon daha karmaşık olabilir
        buffer = (ctypes.c_byte * 50)()
        bytes_read = ctypes.c_size_t()
        
        if kernel32.ReadProcessMemory(
            kernel32.GetCurrentProcess(),
            func_addr,
            buffer,
            50,
            ctypes.byref(bytes_read)
        ):
            # mov eax, imm32 (0xB8) pattern'ini ara
            for i in range(min(20, bytes_read.value - 4)):
                if buffer[i] == 0xB8:
                    syscall_num = int.from_bytes(buffer[i+1:i+5], byteorder='little')
                    return syscall_num
        
        return None
    except Exception as e:
        print(f"[-] Syscall number çıkarılamadı: {e}")
        return None

def test_syscall_detection():
    """Test 2: Syscall Number Detection"""
    print("[*] Test 2: Syscall Number Detection")
    print("    Bu test, ntdll.dll'den syscall number'larını çıkarır.\n")
    
    syscall_num = get_syscall_number("NtCreateFile")
    if syscall_num:
        print(f"[+] NtCreateFile syscall number: 0x{syscall_num:08X} ({syscall_num})")
    else:
        print("[-] Syscall number bulunamadı")
        print("    Not: Bu Windows sürümünde inline syscall kullanılıyor olabilir")
    
    print()

def test_av_detection():
    """Test 3: AV/EDR Detection Test"""
    print("[*] Test 3: AV/EDR Detection Test")
    print("    Bu test, sistemdeki AV/EDR ürünlerini tespit etmeye çalışır.\n")
    
    # Yaygın AV/EDR process'lerini kontrol et
    av_processes = [
        "MsMpEng.exe",      # Windows Defender
        "MsMpEngCP.exe",    # Windows Defender
        "MpCmdRun.exe",     # Windows Defender
        "smartscreen.exe",  # Windows SmartScreen
        "SgrmBroker.exe",   # Windows System Guard
        "SgrmAgent.exe",    # Windows System Guard
        "CrowdStrike",      # CrowdStrike
        "SentinelAgent",    # SentinelOne
        "EDRAgent",         # Generic EDR
        "chomar",           # Chomar Internet Security
        "Chomar",           # Chomar Internet Security
        "chomarsecurity",   # Chomar Security
    ]
    
    print("[*] AV/EDR process'leri kontrol ediliyor...")
    detected = []
    
    # Process listesi al
    try:
        # CreateToolhelp32Snapshot kullan
        TH32CS_SNAPPROCESS = 0x00000002
        h_snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        
        if h_snapshot != -1:
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
            
            if Process32First(h_snapshot, ctypes.byref(pe32)):
                while True:
                    process_name = pe32.szExeFile.decode('utf-8', errors='ignore')
                    for av_proc in av_processes:
                        if av_proc.lower() in process_name.lower():
                            if process_name not in detected:
                                print(f"[!] Tespit edildi: {process_name} (PID: {pe32.th32ProcessID})")
                                detected.append(process_name)
                    
                    if not Process32Next(h_snapshot, ctypes.byref(pe32)):
                        break
            
            kernel32.CloseHandle(h_snapshot)
        
        if not detected:
            print("[+] Bilinen AV/EDR process'i tespit edilmedi")
        else:
            print(f"[!] Toplam {len(detected)} AV/EDR process'i tespit edildi")
            
    except Exception as e:
        print(f"[-] Process listesi alınamadı: {e}")
    
    print()

def save_test_results(filename):
    """Test sonuçlarını dosyaya kaydet"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("User-Mode Syscall Test Sonuçları\n")
            f.write("==================================\n\n")
            f.write(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Python Sürümü: {sys.version}\n")
            f.write(f"İşletim Sistemi: {os.name}\n")
            f.write("\n")
            f.write("Test Senaryoları:\n")
            f.write("1. Normal API Call Test\n")
            f.write("2. Syscall Number Detection\n")
            f.write("3. AV/EDR Detection\n")
            f.write("\n")
            f.write("Not: Bu test sadece eğitim ve araştırma amaçlıdır.\n")
            f.write("Sadece kendi sisteminizde ve yetkili test ortamlarında kullanın.\n")
        
        print(f"[+] Test sonuçları kaydedildi: {filename}")
    except Exception as e:
        print(f"[-] Test sonuçları kaydedilemedi: {e}")

def main():
    print("=" * 50)
    print("User-Mode Syscall Bypass Test Tool (Python)")
    print("=" * 50)
    print()
    print("[!] UYARI: Bu araç sadece kendi sisteminizde ve yetkili test ortamlarında kullanılmalıdır.")
    print("[!] Eğitim ve araştırma amaçlıdır. Zararlı amaçla kullanmayın.")
    print()
    
    # Test dizini oluştur
    test_dir = "C:\\temp"
    if not os.path.exists(test_dir):
        try:
            os.makedirs(test_dir)
        except:
            pass
    
    # Testleri çalıştır
    test_normal_api_call()
    time.sleep(1)  # AV'nin tepkisini gözlemlemek için bekle
    
    test_syscall_detection()
    time.sleep(1)
    
    test_av_detection()
    
    # Sonuçları kaydet
    save_test_results("syscall_test_results.txt")
    
    print()
    print("=" * 50)
    print("Test tamamlandı!")
    print("=" * 50)
    print()
    print("Sonraki adımlar:")
    print("1. AV/EDR loglarını kontrol edin")
    print("2. Event Viewer'da güvenlik olaylarını inceleyin")
    print("3. Test sonuçlarını syscall_test_results.txt dosyasından okuyun")
    print()
    print("AV/EDR tepkisini gözlemlemek için:")
    print("- Windows Defender: Windows Security > Protection history")
    print("- Event Viewer: Windows Logs > Security")
    print("- Task Manager: Process'leri kontrol edin")
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

