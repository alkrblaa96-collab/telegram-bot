import telebot

TOKEN = "7668280359:AAGKEgb6Gd_j5CTLq8xmKSQKkxFqpGzr4D0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "هلا حبيبي البوت شغال 🔥")

print("Bot started...")

bot.infinity_polling()
