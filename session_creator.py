import os
import asyncio
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.auth import ExportLoginTokenRequest
from telethon.tl.types import InputCheckPasswordSRP
import zipfile
import json
import shutil
from pathlib import Path

# Logging ayarı
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramSessionCreator:
    def __init__(self):
        self.sessions_dir = "sessions"
        self.numbers_file = "numbers.txt"
        self.api_id =  # Buraya kendi API ID'nizi girin
        self.api_hash = ""  # Buraya kendi API Hash'inizi girin
        
        # Dizinleri oluştur
        Path(self.sessions_dir).mkdir(exist_ok=True)
        
    def load_numbers(self):
        """Numaraları txt dosyasından yükle"""
        try:
            with open(self.numbers_file, 'r', encoding='utf-8') as f:
                numbers = [line.strip() for line in f if line.strip()]
            return numbers
        except FileNotFoundError:
            logger.error(f"{self.numbers_file} dosyası bulunamadı!")
            return []
    
    async def create_session(self, phone_number):
        """Tek bir numara için session oluştur"""
        try:
            logger.info(f"{phone_number} için session oluşturuluyor...")
            
            # String session oluştur
            client = TelegramClient(
                session=StringSession(),
                api_id=self.api_id,
                api_hash=self.api_hash,
                device_model="Session Creator",
                app_version="1.0.0",
                system_version="Python 3.8+"
            )
            
            await client.connect()
            
            # Telefon numarasını doğrula ve kod iste
            sent_code = await client.send_code_request(phone_number)
            
            # Kullanıcıdan kodu al
            code = input(f"{phone_number} için gelen kodu girin: ")
            
            # Oturumu aç
            await client.sign_in(phone_number, code)
            
            # Session string'ini al
            session_string = client.session.save()
            
            # .session dosyasını kaydet
            session_filename = f"{self.sessions_dir}/{phone_number.replace('+', '')}.session"
            with open(session_filename, 'w', encoding='utf-8') as f:
                f.write(session_string)
            
            # TData klasörü oluştur
            await self.create_tdata(client, phone_number)
            
            await client.disconnect()
            
            logger.info(f"{phone_number} için session başarıyla oluşturuldu!")
            return True
            
        except Exception as e:
            logger.error(f"{phone_number} için hata: {str(e)}")
            return False
    
    async def create_tdata(self, client, phone_number):
        """TData klasörü oluştur"""
        try:
            tdata_dir = f"{self.sessions_dir}/{phone_number.replace('+', '')}_tdata"
            Path(tdata_dir).mkdir(exist_ok=True)
            
            # Basit tdata yapısı oluştur
            # Not: Gerçek tdata yapısı daha karmaşıktır, bu basit bir örnektir
            tdata_structure = {
                "version": "1.0.0",
                "phone": phone_number,
                "api_id": self.api_id,
                "created_by": "@mebularts - https://mebularts.com.tr"
            }
            
            with open(f"{tdata_dir}/config.json", 'w', encoding='utf-8') as f:
                json.dump(tdata_structure, f, indent=2)
            
            # TData'yı zip olarak kaydet
            self.create_tdata_zip(phone_number, tdata_dir)
            
            logger.info(f"{phone_number} için tdata oluşturuldu")
            
        except Exception as e:
            logger.error(f"TData oluşturma hatası: {str(e)}")
    
    def create_tdata_zip(self, phone_number, tdata_dir):
        """TData klasörünü zip olarak sıkıştır"""
        zip_filename = f"{self.sessions_dir}/{phone_number.replace('+', '')}_tdata.zip"
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(tdata_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, tdata_dir)
                    zipf.write(file_path, arcname)
    
    async def process_all_numbers(self):
        """Tüm numaraları işle"""
        numbers = self.load_numbers()
        
        if not numbers:
            logger.error("İşlenecek numara bulunamadı!")
            return
        
        logger.info(f"Toplam {len(numbers)} numara bulundu. İşlem başlatılıyor...")
        
        successful = 0
        failed = 0
        
        for phone_number in numbers:
            # Telefon numarasını temizle ve doğrula
            cleaned_number = self.clean_phone_number(phone_number)
            if not cleaned_number:
                logger.warning(f"Geçersiz numara formatı: {phone_number}")
                failed += 1
                continue
            
            result = await self.create_session(cleaned_number)
            if result:
                successful += 1
            else:
                failed += 1
            
            # API limitlerini aşmamak için bekle
            await asyncio.sleep(2)
        
        logger.info(f"İşlem tamamlandı! Başarılı: {successful}, Başarısız: {failed}")
    
    def clean_phone_number(self, phone_number):
        """Telefon numarasını temizle ve doğrula"""
        # Boşlukları ve özel karakterleri temizle
        cleaned = ''.join(c for c in phone_number if c.isdigit() or c == '+')
        
        # + işareti ile başlamıyorsa ekle
        if not cleaned.startswith('+'):
            # Varsayılan ülke kodu olarak +90 ekleyebilirsiniz
            # cleaned = '+90' + cleaned
            logger.warning(f"Ülke kodu olmayan numara: {phone_number}")
            return None
        
        return cleaned

def main():
    """Ana fonksiyon"""
    print("=" * 50)
    print("Telegram Session Creator Bot")
    print("Developer: @mebularts")
    print("Website: https://mebularts.com.tr")
    print("=" * 50)
    
    creator = TelegramSessionCreator()
    
    # API bilgilerini kontrol et
    if not creator.api_id or not creator.api_hash:
        print("\n⚠️  Lütfen API bilgilerini girin!")
        print("my.telegram.org adresinden API ID ve Hash alabilirsiniz.")
        creator.api_id = int(input("API ID: "))
        creator.api_hash = input("API Hash: ")
    
    # Numaraları kontrol et
    if not os.path.exists(creator.numbers_file):
        print(f"\n📝 {creator.numbers_file} dosyası oluşturuluyor...")
        with open(creator.numbers_file, 'w', encoding='utf-8') as f:
            f.write("# Her satıra bir telefon numarası yazın\n")
            f.write("# Örnek: +901234567890\n")
            f.write("# Örnek: +441234567890\n")
            f.write("# Örnek: +11234567890\n")
        print(f"Lütfen {creator.numbers_file} dosyasını doldurun ve tekrar çalıştırın.")
        return
    
    # İşlemi başlat
    asyncio.run(creator.process_all_numbers())

if __name__ == "__main__":
    main()
