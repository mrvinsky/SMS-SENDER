from twilio.rest import Client
import pandas as pd

# Twilio hesap bilgileri
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Kişi listesini oku
def read_contact_list(filename):
    return pd.read_csv(filename)

# Her kişiye uygun mesajı gönder
def send_custom_sms_to_contacts(contact_list, message_dict):
    for index, row in contact_list.iterrows():
        name = row['Name']
        phone_number = row['Phone']
        special_day = row['Special Day']
        if special_day in message_dict:
            message = message_dict[special_day].format(name=name)
            send_sms(phone_number, message)
        else:
            print("Özel gün için mesaj bulunamadı:", special_day)

# SMS gönder
def send_sms(to, message):
    message = client.messages.create(
                              body=message,
                              from_='YOUR_TWILIO_NUMBER',
                              to=to
                          )

    print("SMS sent to", to)

# Ana fonksiyon
def main():
    contact_list = read_contact_list('contact_list.csv')
    
    # Özel günler ve mesajları
    special_messages = {
        "Birthday": "Sevgili {name}, doğum günün kutlu olsun! 🎂",
        "Anniversary": "Sevgili {name}, yıldönümünüz kutlu olsun! 💑"
        # Buraya istediğiniz kadar özel gün ve mesaj ekleyebilirsiniz
    }
    
    send_custom_sms_to_contacts(contact_list, special_messages)

if __name__ == "__main__":
    main()
