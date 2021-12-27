import requests
def telegram_bot_sendtext(bot_message):
   
    bot_token = '2128421945:AAHz-s9UwmnCoXP4zbcQjTUm5KSS0EtHzl8'
    bot_chatID = '1142557708'
    send_text= 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode = MarkdownV2&text=' +bot_message
   
    response = requests.get(send_text)
    return response.json()
telegram_bot_sendtext("Hello Good Mornining!")
