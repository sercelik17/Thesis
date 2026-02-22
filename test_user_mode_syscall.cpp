/*
 * User-Mode Syscall Bypass Test Tool
 * 
 * Bu araç, Windows'ta user-mode syscall hooking bypass tekniklerini test etmek için tasarlanmıştır.
 * Sadece kendi sisteminizde ve yetkili test ortamlarında kullanın.
 * 
 * Test: Direct syscall kullanarak NtCreateFile API'sini çağırır ve AV/EDR tepkisini gözlemler.
 */

#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#include <string.h>

// NtCreateFile syscall number (Windows 10/11 için - farklı Windows sürümlerinde değişebilir)
#define SYSCALL_NT_CREATE_FILE 0x0055

// NtCreateFile function signature
typedef NTSTATUS (NTAPI *pNtCreateFile)(
    PHANDLE FileHandle,
    ACCESS_MASK DesiredAccess,
    POBJECT_ATTRIBUTES ObjectAttributes,
    PIO_STATUS_BLOCK IoStatusBlock,
    PLARGE_INTEGER AllocationSize,
    ULONG FileAttributes,
    ULONG ShareAccess,
    ULONG CreateDisposition,
    ULONG CreateOptions,
    PVOID EaBuffer,
    ULONG EaLength
);

// Direct syscall implementation (inline assembly veya MASM)
// Not: Modern derleyicilerde inline assembly kullanımı sınırlıdır
// Bu yüzden MASM dosyası veya external assembly kullanılmalıdır

// Basit test: Normal API çağrısı ile başlayalım
void test_normal_api_call() {
    printf("[*] Test 1: Normal API Call (NtCreateFile via ntdll.dll)\n");
    printf("    Bu test, normal API çağrısını kullanır ve AV'nin tepkisini gözlemler.\n\n");
    
    HMODULE hNtdll = GetModuleHandleA("ntdll.dll");
    if (!hNtdll) {
        printf("[-] ntdll.dll yüklenemedi\n");
        return;
    }
    
    pNtCreateFile NtCreateFile = (pNtCreateFile)GetProcAddress(hNtdll, "NtCreateFile");
    if (!NtCreateFile) {
        printf("[-] NtCreateFile fonksiyonu bulunamadı\n");
        return;
    }
    
    printf("[+] NtCreateFile adresi: 0x%p\n", NtCreateFile);
    printf("[+] Test dosyası oluşturuluyor...\n");
    
    // Test dosyası oluştur
    HANDLE hFile = NULL;
    OBJECT_ATTRIBUTES objAttr;
    IO_STATUS_BLOCK ioStatus;
    UNICODE_STRING fileName;
    WCHAR filePath[] = L"\\??\\C:\\temp\\syscall_test.txt";
    
    RtlInitUnicodeString(&fileName, filePath);
    InitializeObjectAttributes(&objAttr, &fileName, OBJ_CASE_INSENSITIVE, NULL, NULL);
    
    NTSTATUS status = NtCreateFile(
        &hFile,
        FILE_GENERIC_WRITE,
        &objAttr,
        &ioStatus,
        NULL,
        FILE_ATTRIBUTE_NORMAL,
        0,
        FILE_OVERWRITE_IF,
        FILE_NON_DIRECTORY_FILE,
        NULL,
        0
    );
    
    if (NT_SUCCESS(status)) {
        printf("[+] Dosya başarıyla oluşturuldu (Normal API)\n");
        CloseHandle(hFile);
        DeleteFileW(L"C:\\temp\\syscall_test.txt");
    } else {
        printf("[-] Dosya oluşturulamadı. Status: 0x%08X\n", status);
    }
    
    printf("\n");
}

// Syscall number'ı ntdll.dll'den çıkar
DWORD get_syscall_number(const char* functionName) {
    HMODULE hNtdll = GetModuleHandleA("ntdll.dll");
    if (!hNtdll) {
        return 0;
    }
    
    FARPROC funcAddr = GetProcAddress(hNtdll, functionName);
    if (!funcAddr) {
        return 0;
    }
    
    // NtCreateFile için syscall number'ı bellekten oku
    // Windows'ta syscall instruction'dan önceki mov eax, <syscall_number> komutunu bul
    BYTE* bytes = (BYTE*)funcAddr;
    
    // Basit pattern matching (mov eax, XX)
    for (int i = 0; i < 20; i++) {
        if (bytes[i] == 0xB8) { // mov eax, imm32
            DWORD syscallNum = *(DWORD*)(bytes + i + 1);
            return syscallNum;
        }
    }
    
    return 0;
}

void test_syscall_detection() {
    printf("[*] Test 2: Syscall Number Detection\n");
    printf("    Bu test, ntdll.dll'den syscall number'larını çıkarır.\n\n");
    
    DWORD syscallNum = get_syscall_number("NtCreateFile");
    if (syscallNum != 0) {
        printf("[+] NtCreateFile syscall number: 0x%08X (%u)\n", syscallNum, syscallNum);
    } else {
        printf("[-] Syscall number bulunamadı\n");
    }
    
    printf("\n");
}

// AV/EDR tespit testi
void test_av_detection() {
    printf("[*] Test 3: AV/EDR Detection Test\n");
    printf("    Bu test, sistemdeki AV/EDR ürünlerini tespit etmeye çalışır.\n\n");
    
    // Yaygın AV/EDR process'lerini kontrol et
    const char* av_processes[] = {
        "MsMpEng.exe",      // Windows Defender
        "MsMpEngCP.exe",    // Windows Defender
        "MpCmdRun.exe",     // Windows Defender
        "smartscreen.exe",  // Windows SmartScreen
        "SgrmBroker.exe",   // Windows System Guard
        "SgrmAgent.exe",    // Windows System Guard
        NULL
    };
    
    printf("[*] AV/EDR process'leri kontrol ediliyor...\n");
    int detected = 0;
    
    for (int i = 0; av_processes[i] != NULL; i++) {
        HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if (hSnapshot == INVALID_HANDLE_VALUE) {
            continue;
        }
        
        PROCESSENTRY32 pe32;
        pe32.dwSize = sizeof(PROCESSENTRY32);
        
        if (Process32First(hSnapshot, &pe32)) {
            do {
                if (_stricmp(pe32.szExeFile, av_processes[i]) == 0) {
                    printf("[!] Tespit edildi: %s (PID: %u)\n", av_processes[i], pe32.th32ProcessID);
                    detected++;
                }
            } while (Process32Next(hSnapshot, &pe32));
        }
        
        CloseHandle(hSnapshot);
    }
    
    if (detected == 0) {
        printf("[+] Bilinen AV/EDR process'i tespit edilmedi\n");
    } else {
        printf("[!] Toplam %d AV/EDR process'i tespit edildi\n", detected);
    }
    
    printf("\n");
}

// Test sonuçlarını dosyaya kaydet
void save_test_results(const char* filename) {
    FILE* f = fopen(filename, "w");
    if (!f) {
        printf("[-] Test sonuçları kaydedilemedi\n");
        return;
    }
    
    fprintf(f, "User-Mode Syscall Test Sonuçları\n");
    fprintf(f, "==================================\n\n");
    fprintf(f, "Tarih: %s\n", __DATE__);
    fprintf(f, "Saat: %s\n", __TIME__);
    fprintf(f, "\n");
    fprintf(f, "Test Senaryoları:\n");
    fprintf(f, "1. Normal API Call Test\n");
    fprintf(f, "2. Syscall Number Detection\n");
    fprintf(f, "3. AV/EDR Detection\n");
    fprintf(f, "\n");
    fprintf(f, "Not: Bu test sadece eğitim ve araştırma amaçlıdır.\n");
    
    fclose(f);
    printf("[+] Test sonuçları kaydedildi: %s\n", filename);
}

int main() {
    printf("========================================\n");
    printf("User-Mode Syscall Bypass Test Tool\n");
    printf("========================================\n\n");
    
    printf("[!] UYARI: Bu araç sadece kendi sisteminizde ve yetkili test ortamlarında kullanılmalıdır.\n");
    printf("[!] Eğitim ve araştırma amaçlıdır. Zararlı amaçla kullanmayın.\n\n");
    
    // Test dizini oluştur
    CreateDirectoryA("C:\\temp", NULL);
    
    // Testleri çalıştır
    test_normal_api_call();
    test_syscall_detection();
    test_av_detection();
    
    // Sonuçları kaydet
    save_test_results("syscall_test_results.txt");
    
    printf("\n========================================\n");
    printf("Test tamamlandı!\n");
    printf("========================================\n");
    
    printf("\nSonraki adımlar:\n");
    printf("1. AV/EDR loglarını kontrol edin\n");
    printf("2. Event Viewer'da güvenlik olaylarını inceleyin\n");
    printf("3. Test sonuçlarını syscall_test_results.txt dosyasından okuyun\n");
    
    system("pause");
    return 0;
}

