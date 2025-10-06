# Telegram Session Creator Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telethon](https://img.shields.io/badge/Telethon-1.28+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Advanced Telegram Session Generator with Multi-Format Support**

[![Features](https://img.shields.io/badge/Features-.session%20%7C%20tdata%20%7C%20Multi--Country-orange.svg)](https://github.com/mebularts/telegram-session-creator)
[![Developer](https://img.shields.io/badge/Developer-@mebularts-purple.svg)](https://mebularts.com.tr)

</div>

## 🌟 Özellikler

### 🚀 Temel Özellikler
- ✅ **Tüm Ülke Kodları Desteği** (+1, +44, +90, +7, +49, vb.)
- ✅ **Çift Format Desteği** - `.session` ve `tdata` dosyaları
- ✅ **Toplu İşlem** - Tek seferde çoklu numara işleme
- ✅ **Otomatik Format Temizleme** - Girdi doğrulama ve temizleme
- ✅ **Detaylı Loglama** - İşlem takibi ve hata yönetimi

### 🛠 Gelişmiş Özellikler
- 🔒 **Güvenli Kimlik Doğrulama**
- 📁 **Otomatik Klasör Yönetimi**
- 🗜 **TData Zip Sıkıştırma**
- ⚡ **Asenkron İşlemler**
- 🎯 **API Limit Yönetimi**

## 📦 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- Telegram API erişimi

### Hızlı Kurulum

```bash
# Repository'yi klonlayın
git clone https://github.com/mebularts/telegram-session-creator.git
cd telegram-session-creator

# Gerekli paketleri yükleyin
pip install -r requirements.txt
```

### Manuel Kurulum

```bash
# Telethon kütüphanesini yükleyin
pip install telethon==1.28.5
```

## ⚡ Hızlı Başlangıç

### 1. API Bilgilerini Alın
```python
# my.telegram.org adresinden alın
API_ID = 1234567
API_HASH = "your_api_hash_here"
```

### 2. Numaraları Hazırlayın
`numbers.txt` dosyasını oluşturun:
```txt
# Her satıra bir telefon numarası
+901234567890
+441234567890
+11234567890
+79123456789
```

### 3. Botu Çalıştırın
```bash
python session_creator.py
```

## 📁 Dosya Yapısı

```
telegram-session-creator/
├── session_creator.py      # Ana uygulama
├── requirements.txt        # Bağımlılıklar
├── numbers.txt            # Telefon numaraları
├── sessions/              # Oluşturulan sessionlar
│   ├── 901234567890.session
│   ├── 901234567890_tdata.zip
│   ├── 441234567890.session
│   └── 441234567890_tdata.zip
└── README.md
```

## 🔧 Kullanım

### Temel Kullanım
```python
from session_creator import TelegramSessionCreator

# Session oluşturucuyu başlat
creator = TelegramSessionCreator()

# Tüm numaraları işle
await creator.process_all_numbers()
```

### Gelişmiş Kullanım
```python
# Özel API bilgileri ile
creator = TelegramSessionCreator()
creator.api_id = YOUR_API_ID
creator.api_hash = YOUR_API_HASH

# Özel session dizini
creator.sessions_dir = "my_sessions"
```

## 🎯 Örnek Çıktı

```bash
==================================================
Telegram Session Creator Bot
Developer: @mebularts
Website: https://mebularts.com.tr
==================================================

📱 +901234567890 için session oluşturuluyor...
✅ +901234567890 için session başarıyla oluşturuldu!
📦 +901234567890 için tdata oluşturuldu

📱 +441234567890 için session oluşturuluyor...
✅ +441234567890 için session başarıyla oluşturuldu!
📦 +441234567890 için tdata oluşturuldu

🎉 İşlem tamamlandı! Başarılı: 2, Başarısız: 0
```

## 🔒 Güvenlik

- 🔐 Session dosyalarını güvenli yerde saklayın
- 🚫 API bilgilerinizi paylaşmayın
- 📱 2FA etkin hesaplar için ek doğrulama gerekir

## 🌍 Desteklenen Ülke Kodları

| Ülke | Kod | Örnek |
|------|-----|-------|
| Türkiye | +90 | +901234567890 |
| ABD/Kanada | +1 | +11234567890 |
| İngiltere | +44 | +441234567890 |
| Rusya | +7 | +79123456789 |
| Almanya | +49 | +491234567890 |
| Fransa | +33 | +33123456789 |
| Ve diğerleri... | | |

## 🐛 Sorun Giderme

### Sık Karşılaşılan Sorunlar

1. **API Hatası**
   ```bash
   # API bilgilerini kontrol edin
   # my.telegram.org'dan yeni API anahtarları alın
   ```

2. **Doğrulama Kodu Hatası**
   ```bash
   # Telefon numarası formatını kontrol edin
   # Ülke kodunun doğru olduğundan emin olun
   ```

3. **Rate Limit**
   ```bash
   # İşlemler arasında bekleme süresini artırın
   # await asyncio.sleep(5)  # 5 saniye bekle
   ```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**@mebularts**

- 🌐 Website: [https://mebularts.com.tr](https://mebularts.com.tr)
- 📧 Telegram: [t.me/mebularts](t.me/mebularts)
- 📱 WhatsApp: [wa.me/12513160268](wa.me/12513160268)

## ⭐ Destek

Eğer bu projeyi faydalı bulduysanız, bir ⭐ vererek destek olabilirsiniz!

---

<div align="center">

**⚠️ Uyarı: Bu araç sadece eğitim amaçlıdır. Lütfen Telegram'ın ToS kurallarına uygun kullanın.**

[![GitHub stars](https://img.shields.io/github/stars/mebularts/telegram-session-creator?style=social)](https://github.com/mebularts/telegram-session-creator)
[![GitHub forks](https://img.shields.io/github/forks/mebularts/telegram-session-creator?style=social)](https://github.com/mebularts/telegram-session-creator)

</div>
