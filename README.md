Tabii, reponun adını "SMS-SENDER" olarak değiştirelim. Açıklamayı da bu değişikliği yansıtacak şekilde güncelleyelim. İşte güncellenmiş bir GitHub reposu açıklama örneği:

---

# Twilio ile Otomatik SMS Gönderici

Bu proje, Python ve Twilio kullanarak özel günlerde otomatik SMS gönderen bir botu içerir. Proje, verilen bir kişi listesindeki her bir kişiye, doğum günü, yıldönümü gibi özel günlerde kişiye özel olarak tanımlanan mesajları gönderir.

## Nasıl Çalışır?

1. **Kişi Listesi**: Proje, `contact_list.csv` adında bir dosyadan kişi bilgilerini okur. Bu dosyada her bir kişi için ad, telefon numarası ve özel gün bilgileri bulunmalıdır.

2. **Özel Günler ve Mesajlar**: Her özel gün için, gönderilecek mesajlar bir sözlükte belirtilir. Örneğin, doğum günleri için "Sevgili {name}, doğum günün kutlu olsun! 🎂" gibi mesajlar belirlenebilir.

3. **SMS Gönderme**: Proje, Twilio API'sini kullanarak belirlenen mesajları ilgili kişilere gönderir.

## Kurulum

1. Bu projeyi klonlayın: `git clone https://github.com/mrvinsky/SMS-SENDER.git`
2. `cd SMS-SENDER`
3. Gerekli Python kütüphanelerini yükleyin: `pip install -r requirements.txt`
4. `config.py` dosyasını oluşturun ve Twilio hesap bilgilerinizi ve diğer ayarları girin.

## Kullanım

1. Kişi listesi dosyasını `contact_list.csv` olarak projenin kök dizinine ekleyin. 
2. Projeyi çalıştırın: `python main.py`

## Örnek Kişi Listesi Formatı (contact_list.csv)

| Name       | Phone         | Special Day |
|------------|---------------|-------------|
| John Doe   | +12345678901  | Birthday    |
| Jane Smith | +19876543210  | Anniversary |
| ...        | ...           | ...         |

## Gereksinimler

- Python 3.x
- Twilio hesabı ve API anahtarı

## Katkı

Herhangi bir katkı veya geribildirim çok değerlidir. Projeyle ilgili herhangi bir sorunuz, öneriniz veya isteğiniz varsa lütfen [issue tracker](https://github.com/mrvinsky/SMS-SENDER/issues) kullanarak bize bildirin.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atın.

---

