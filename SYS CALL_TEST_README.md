# User-Mode Syscall Bypass Test Tool

Bu araç, Windows'ta user-mode syscall hooking bypass tekniklerini test etmek için tasarlanmıştır.

## ⚠️ ÖNEMLİ UYARILAR

- **Sadece kendi sisteminizde ve yetkili test ortamlarında kullanın**
- **Eğitim ve araştırma amaçlıdır**
- **Zararlı amaçla kullanmayın**
- **Test ortamınızda yedek alın**

## 📋 Gereksinimler

### Python Versiyonu için:
- Python 3.6+
- Windows 10/11
- Yönetici hakları (bazı testler için)

### C++ Versiyonu için:
- MinGW-w64 veya Visual Studio
- Windows 10/11
- Yönetici hakları (bazı testler için)

## 🚀 Kullanım

### Python Versiyonu (Önerilen)

```bash
python test_user_mode_syscall.py
```

### C++ Versiyonu

1. Derleme:
```bash
build_syscall_test.bat
```

2. Çalıştırma:
```bash
test_user_mode_syscall.exe
```

## 🧪 Test Senaryoları

### Test 1: Normal API Call
- `NtCreateFile` API'sini normal yöntemle çağırır
- AV/EDR'ın tepkisini gözlemler
- Test dosyası oluşturur ve siler

### Test 2: Syscall Number Detection
- `ntdll.dll`'den syscall number'larını çıkarır
- Direct syscall için gerekli bilgileri toplar

### Test 3: AV/EDR Detection
- Sistemde çalışan AV/EDR process'lerini tespit eder
- Yaygın güvenlik ürünlerini arar

## 📊 Sonuçlar

Test sonuçları `syscall_test_results.txt` dosyasına kaydedilir.

## 🔍 AV/EDR Tepkisini Gözlemleme

### Windows Defender
1. Windows Security > Protection history
2. Event Viewer > Windows Logs > Security
3. Task Manager > Details sekmesi

### Diğer AV/EDR Ürünleri
- Ürünün kendi log/event viewer'ını kontrol edin
- Real-time protection loglarını inceleyin

## 📝 Test Sonrası Kontroller

1. **AV/EDR Logları**: Tespit edilen aktiviteleri kontrol edin
2. **Event Viewer**: Windows güvenlik olaylarını inceleyin
3. **Process Monitor**: Syscall'ları gerçek zamanlı izleyin (opsiyonel)
4. **Network Activity**: Şüpheli ağ bağlantılarını kontrol edin

## 🛠️ Gelişmiş Kullanım

### Direct Syscall Implementation

Gerçek direct syscall implementasyonu için:
- MASM (Microsoft Macro Assembler) kullanın
- Hell's Gate / Halo's Gate tekniklerini araştırın
- Syscall number'ları dinamik olarak çıkarın

### Örnek Direct Syscall (C++)

```cpp
// Bu örnek sadece kavramsal amaçlıdır
// Gerçek implementasyon daha karmaşıktır

__declspec(naked) NTSTATUS NtCreateFileDirect(...) {
    __asm {
        mov eax, SYSCALL_NUMBER
        mov r10, rcx
        syscall
        ret
    }
}
```

## 📚 Kaynaklar

- [Windows Syscalls](https://j00ru.vexillium.org/syscalls/nt/64/)
- [Hell's Gate Technique](https://github.com/am0nsec/HellsGate)
- [Halo's Gate Technique](https://github.com/am0nsec/HellsGate)

## ⚖️ Yasal Uyarı

Bu araç sadece:
- Kendi sisteminizde test için
- Yetkili penetrasyon testleri için
- Eğitim ve araştırma amaçlı

kullanılmalıdır. Yetkisiz sistemlerde kullanım yasalara aykırıdır.

## 🐛 Sorun Giderme

### "Access Denied" Hatası
- Yönetici olarak çalıştırın
- UAC'yi kontrol edin

### "Module not found" Hatası
- Python sürümünü kontrol edin
- Gerekli modüllerin yüklü olduğundan emin olun

### AV Tarafından Engellenme
- Test dosyasını AV istisnasına ekleyin
- Test ortamında AV'yi geçici olarak kapatın (sadece test için)

## 📧 İletişim

Sorularınız için proje repository'sinde issue açabilirsiniz.

---

**Not**: Bu araç sürekli geliştirilmektedir. Yeni özellikler ve iyileştirmeler için güncellemeleri takip edin.

