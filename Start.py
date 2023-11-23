start_message = bot.send_message(chat_id, "Smsler Gönderiliyor...")

    
    response = requests.get(api_url)

    if response.status_code == 200:
        
        bot.send_message(chat_id, "Smsler Başarılı Bir Şekilde Gönderildi!\n\nSistem Projessor </>")
    else:
        bot.send_message(chat_id, "SMS gönderirken bir hata oluştu.") # @menrosee

    
    bot.delete_message(chat_id, start_message.message_id)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e}")
