import telebot
from covid import Covid
from telebot import types


covid = Covid(source='worldometers')

TOKEN = "1687352369:AmoM8u7-dt1V7NvtPac"
bot = telebot.TeleBot(TOKEN)

btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Statistika")
btn2 = types.KeyboardButton("Dunyo")

btn.row(btn1, btn2)


@bot.message_handler(commands=['start'])
def start(message):
	text = "<b>Salom hurmatli foydalanuvchi. Marhamat, tanlang...</b>"
	bot.send_message(message.chat.id, text, reply_markup=btn, parse_mode="HTML")
	
@bot.message_handler(func=lambda message: True)
def stats(message):
	msg = message.text.casefold()
	if msg == "statistika":
	  data = covid.get_status_by_country_name('Uzbekistan')
	  text = "<b>O'zbekiston statistikasi</b>\n"
	  text += "\n<b>Yuqtirganlar:</b> {}".format("{:,}".format(data['confirmed']))
	  text += "\n<b>Davolanganlar:</b> {}".format("{:,}".format(data['recovered']))
	  text += "\n<b>Ko'z yumganlar:</b> {}".format(data['deaths'])
	  bot.send_message(message.chat.id, text, reply_markup=btn, parse_mode="HTML")
		
	elif msg == "dunyo":
		data = covid.get_total_confirmed_cases()
		data2 = covid.get_total_recovered()
		data3 = covid.get_total_deaths()
		text = "<b>Dunyo statistikasi</b>\n"
		text += "\n<b>Yuqtirganlar:</b> {}".format("{:,}".format(data))
		text += "\n<b>Davolanganlar:</b> {}".format("{:,}".format(data2))
		text += "\n<b>Ko'z yumganlar:</b> {}".format("{:,}".format(data3))
		bot.send_message(message.chat.id, text, reply_markup=btn, parse_mode="HTML")
		
	else:
	  text = "Qandaydir xato bor"
	  bot.reply_to(message, text, reply_markup=btn)
		
bot.polling()
