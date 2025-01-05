Discord Pokémon Botu
Bu proje, Discord'da kullanıcıların Pokémon oluşturup beslemesine, saldırmasına ve oyunlaştırılmış bir deneyim yaşamasına olanak tanıyan bir bot içerir. Proje, farklı Python modülleri ve sınıfları ile yapılandırılmıştır.

Özellikler
Pokémon Oluşturma: Kullanıcılar !go komutu ile kendilerine bir Pokémon oluşturabilirler.
Pokémon Besleme: Kullanıcılar !feed komutu ile Pokémonlarını besleyebilir ve canlarını artırabilirler.
Pokémon Saldırısı: Pokémonlar diğer Pokémonlara saldırarak hasar verebilir.
Pokémon Görselleri: Bot, Pokémonların görsellerini PokeAPI'den çekip kullanıcılara gösterir.
Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki araçlara ihtiyaç vardır:

Python 3.7 veya üstü
discord.py modülü
aiohttp modülü
requests modülü
Kurulum
Bu repository'yi klonlayın:

bash
Kodu kopyala
git clone <repository-url>
Gerekli Python paketlerini yükleyin:

bash
Kodu kopyala
pip install discord.py aiohttp requests
config.py dosyasına Discord botunuzun token bilgisini ekleyin:

token = "Botunuzun tokenını buraya yapıştırın"
Botu başlatmak için aşağıdaki komutu çalıştırın:

Kullanım
Komutlar
!go: Yeni bir Pokémon oluşturur.
!feed: Pokémon'u besler ve canını artırır.
Proje Dosyaları
config.py: Bot tokenını içeren dosya.
deneme.py: API'den veri çekme ile ilgili örnek bir dosya.
logic.py: Pokémon sınıflarını ve iş mantığını içeren dosya.
main.py: Discord botunun ana dosyası.
API Entegrasyonu
Proje, PokeAPI ile entegre edilmiştir. API, Pokémon bilgilerini ve görsellerini çekmek için kullanılır.

Katkıda Bulunma
Repository'yi fork edin.
Yeni bir branch oluşturun: git checkout -b yeni-ozellik.
Değişikliklerinizi commit edin: git commit -m "Yeni özellik eklendi".
Branch'i push edin: git push origin yeni-ozellik.
Pull Request açın.
