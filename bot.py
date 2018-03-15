from telebot import TeleBot
from bingtts import Translator

telegram_token = '<TELEGRAM_TOKEN>'
azure_token = '<AZURE_TOKEN>'

telebot = TeleBot(telegram_token)
translator = Translator(azure_token)

@telebot.message_handler(content_types=['text'])
def handle_speech(message):
    user_id = message.chat.id
    text = message.text

    speech = translator.speak(text, "en-US", "BenjaminRUS",
                              "audio-16khz-32kbitrate-mono-mp3")
    res = telebot.send_voice(user_id, speech)

if __name__ == '__main__':
    telebot.polling(none_stop=True)
