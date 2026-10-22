import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "8851947928:AAGCu9850VUAo1aK8ZXcAlgo12F_UIbuf2M"
GEMINI_API_KEY = "AIzaSyDSBFirYxmsE63D7QIIFGNWsV0lhKN5EzE"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت ذكاء اصطناعي جاهز للإجابة على أسئلتك.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء معالجة طلبك.")

bot.infinity_polling()
