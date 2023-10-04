python
import telebot

bot = telebot.TeleBot("6556454971:AAE8kkvnqc_t3RIbwiiiMdcDGy1lYNdilcs")

@bot.message_handler(commands=['start'])
def send_welcome(message):
bot.reply_to(message, "Добро пожаловать в калькулятор!")

@bot.message_handler(func=lambda message: True)
def calculate(message):
try:
result = eval(message.text)
bot.reply_to(message, f"Результат: {result}")
except:
bot.reply_to(message, "Произошла ошибка. Пожалуйста, введите корректное выражение.")

bot.polling()