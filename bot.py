import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# sti = open('static/welcome.webp', 'rb')
	# bot.send_sticker(message.chat.id, sti)

	# keyboard
	"""
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Рандомное число")
	item2 = types.KeyboardButton("😊 Как дела?")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

	"""

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Начать тест")
	markup.add(item1)

	bot.send_message(message.chat.id, "Посмотрим, что ты знаешь про коронавирус и все остальное", parse_mode = 'html', reply_markup = markup)


@bot.message_handler(commands=['search'])
def search(message):

	bot.send_message(message.chat.id, "Вот тебе 3 источника информации. Выбери из них самый надежный и рассмотри картинки получше.", parse_mode='html')
	bot.send_message(message.chat.id,
					 "https://pikabu.ru/tag/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/hot",
					 parse_mode='html')
	bot.send_message(message.chat.id,
					 "https://www.bbc.com/russian/news-52085872",
					 parse_mode='html')
	bot.send_message(message.chat.id,
					 "https://vk.com/podslushanotob?w=wall-136862068_839765",
					 parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
	"""
	if message.chat.type == 'private':
		if message.text == '🎲 Рандомное число':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
	"""

	if message.chat.type == 'private':
		if message.text == 'Начать тест':
			markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Джеки Чан")
			item2 = types.KeyboardButton("Си Дзинь Пинь")
			item3 = types.KeyboardButton("Ли Вэнлиань")
			item4 = types.KeyboardButton("Евгений Басков")
			markup_1.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, "Кто обнаружил коронавирус?",
							 parse_mode='html', reply_markup=markup_1)

		elif message.text == "Ли Вэнлиань":
			markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Марс")
			item2 = types.KeyboardButton("Земля")
			item3 = types.KeyboardButton("Юпитер")
			item4 = types.KeyboardButton("Солнце")
			markup_2.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, "На какой планете появился этот вирус впервые?",
							 parse_mode='html', reply_markup=markup_2)

		elif message.text == "Земля":
			markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Coronavirus Disease")
			item2 = types.KeyboardButton("Cola Video")
			item3 = types.KeyboardButton("Coronavirus Disaster")
			item4 = types.KeyboardButton("Coronavirus Destroyer")
			markup_3.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Расшифруйте "COVID": ',
							 parse_mode='html', reply_markup=markup_3)

		elif message.text == "Coronavirus Disease":
			markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Боль в колене")
			item2 = types.KeyboardButton("Обильные кровотечения")
			item3 = types.KeyboardButton("Нарушение нервной системы")
			item4 = types.KeyboardButton("Одышка")
			markup_4.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Выберите симптом коронавируса: ',
							 parse_mode='html', reply_markup=markup_4)

		elif message.text == "Одышка":
			markup_5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('В. Путин: "Если драка неизбежна, бить надо первым"')
			item2 = types.KeyboardButton("С такими спецами не летать нам к далекому космосу...")
			item3 = types.KeyboardButton("кто дудосит тот вонючка")
			item4 = types.KeyboardButton("Отвечать дудосом на дудос")
			markup_5.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Как надо отвечать если сервер дудосят?',
						 parse_mode='html', reply_markup=markup_5)

		elif message.text in ['В. Путин: "Если драка неизбежна, бить надо первым"',
							  "С такими спецами не летать нам к далекому космосу...",
							  "кто дудосит тот вонючка",
							  "Отвечать дудосом на дудос"]:
			bot.send_message(message.chat.id, 'Вариант 3 был правильным по мнению оргов...',
							 parse_mode='html')
			markup_6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Да')
			item2 = types.KeyboardButton('Нет')
			item3 = types.KeyboardButton("Что?")
			item4 = types.KeyboardButton("Ладно!")
			markup_6.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Помогает ли курение как защита от коронавируса',
						 parse_mode='html', reply_markup=markup_6)



		elif message.text == "Нет":
			markup_7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Нет, но сейчас побегу')
			item2 = types.KeyboardButton("Нет, я не поддаюсь панике")
			item3 = types.KeyboardButton("Нет, я вложил все в туалетную бумагу")
			item4 = types.KeyboardButton("Да.")
			markup_7.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Закупили ли вы 500 килограммов гречи?',
						 parse_mode='html', reply_markup=markup_7)

		elif message.text in ['Нет, но сейчас побегу',
							  "Нет, я не поддаюсь панике",
							  "Нет, я вложил все в туалетную бумагу",
							  "Да."]:
			bot.send_message(message.chat.id, 'Понимаю...',
							 parse_mode='html')
			markup_8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('27 938')
			item2 = types.KeyboardButton('32 008')
			item3 = types.KeyboardButton("36 793")
			item4 = types.KeyboardButton("42 853")
			markup_8.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Сколько подтвержденных случаев заражения коронавирусом насчитывалось в России 18 апреля?',
						 parse_mode='html', reply_markup=markup_8)

		elif message.text == "36 793":
			markup_9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Россия')
			item2 = types.KeyboardButton("Китай")
			item3 = types.KeyboardButton("Италия")
			item4 = types.KeyboardButton("США")
			markup_9.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'В какой стране самое большое количество заболевших на апрель 2020 года?',
						 parse_mode='html', reply_markup=markup_9)

		elif message.text == 'США':
			markup_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
			bot.send_message(message.chat.id, 'Допиши фразу: А мыть руки .... . .....!',
							 parse_mode='html', reply_markup=markup_0)


		elif message.text.lower() in "надо с мылом!":
			bot.send_message(message.chat.id, "Твой заслуженный ключ: KEY_2:SO4P_OP3R4")


		else:

			markup_restart = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Начать тест")
			markup_restart.add(item1)
			bot.send_message(message.chat.id, "Чел.... ты....... провалил тест...... Начинай сначала, напиши команду /start, не позорься",  #  + str(message.text == 'США'),
							 parse_mode='html', reply_markup=markup_restart)





# RUN
bot.polling(none_stop=True)