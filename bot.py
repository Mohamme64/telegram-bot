import telebot
from telebot import types

TOKEN = "8622806109:AAEMiNF8RkVWSj6KDGqhSO7DZpSiFJnFtlU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton("📋 القائمة")
    b2 = types.KeyboardButton("📞 المطور")
    b3 = types.KeyboardButton("ℹ️ المساعدة")

    markup.row(b1, b2)
    markup.row(b3)

    bot.send_message(
        message.chat.id,
        "🌹 أهلاً بيك، اختر من الأزرار:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def buttons(message):
    if message.text == "📋 القائمة":
        bot.reply_to(message, "هذه القائمة الرئيسية")

    elif message.text == "📞 المطور":
        bot.reply_to(message, "@اسم_المطور")

    elif message.text == "ℹ️ المساعدة":
        bot.reply_to(message, "شلون أكدر أساعدك؟")

bot.infinity_polling()