import telebot
import requests
from bs4 import BeautifulSoup as BS
import json # чтобы работать с json объектами
import webbrowser # это библиотека взаимодействует с веб сайтами он открывает веб сайты
from telebot import types # это функция создает кнопки
import sqlite3 # для работы с базом данных
# from aiogram import Bot, Dispatcher, executor, types
# сюда мы вставляем токен нашего бота чтобы подключиться
# header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
bot = telebot.TeleBot('6330365444:AAES3KDt80zvJQ7PeHvJcqskpLbfnnNg2YA')
# dp = Dispatcher(bot)


"====================LESSON 7pi============================================"




# executor.start_polling(dp)
"====================LESSON 6======================================="
# amount = 0
# # Бот для конвертации валют
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, введите сумму')
#     bot.register_next_step_handler(message, summa)

# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный фармат. Впишите сумму') # reply_markup=markup этот код добавил именно наши кнопки 
#         bot.register_next_step_handler(message, summa)
#         return

#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2) # тут создалось строчные кнопки которые в одной строке стоят по две
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='asd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='asd/gbp')
#         btn4 = types.InlineKeyboardButton('другая валюта', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup) # reply_markup=markup этот код добавил именно наши кнопки 
#     else:
#         bot.send_message(message.chat.id, 'Сумма должен быть больше чем 0. Введите сумму')
#         bot.register_next_step_handler(message, summa)

# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     values = call.data.upper().split('/')
#     response = requests.get(f'https://www.google.com/finance/quote/{values[0]}-{values[1]}?sa=X&ved=2ahUKEwierKTbiNqCAxXCGxAIHaeICXQQmY0JegQIBhAr', headers=header)
#     soup = BS(response.text, 'lxml')
#     name = soup.find('div', class_='zzDege')
#     summ = soup.find('div', class_='YMlKec fxKbKc')
#     bot.send_message(call.message.chat.id, f'Получается: {name} сейчас {summ}. Можете заново ввести сумму')
#     bot.register_next_step_handler(call.message, summa)




"=====================LESSON 5=============================="
# погоды во всех городах мира 
# API = 'ecf34886dd9415b30b8d8aaa8bccf554'  # здесь я зарегистрировалась к сайту API  погоды и это мой токен

# @bot.message_handler(commands=['start']) # создаем команду /start
# def start(message):
#     bot.send_message(message.chat.id, 'Привет рад тебя видеть, напиши название города') 
#     # для начало он отвечает на команду старт

# @bot.message_handler(content_types=['text']) # затем он вводит название города 
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     # отправляем запрос по указанному тексту тоесть название города 
#     if res.status_code == 200: # если статус кода равен 200 то все верно тоесть он нашел город
#         data = json.loads(res.text) # переводим в язык питон так как он возвращает в json формате
#         temp = data['main']['temp'] # находим ту самую температуру по вложенным словарям или спискам
#         bot.reply_to(message, f"сейчас в городе {city}, {temp} градусов") # отвечаем на его же сообщение и подставляем температуру
#         image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlCcfig8hFgljskcb5qrPIpgc8vFHlO_Kv_GIRTI7ZH4u49vVksT3ztSG890s8K5qNucQ&usqp=CAU' if temp>12 else 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDg0zLfJx4utqiaU5oOsu-k5IOTZYVaRgeTw&usqp=CAU'
#         bot.send_photo(message.chat.id, image) # отправляем соответствующее фото к данной погоде
#     else: # если не найдет город с таким названием
#         bot.reply_to(message, 'Указан не правильный город')




"=====================LESSON 4=========БАЗА ДАННЫХ============"

# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('itproger_telegram.sql') # sqlite3.connect - создает файл если его не существует с расширением sql 
#     cur = conn.cursor() # так мы создали курсор с помощю него мы можем проделывать различные команды связанные с базой данных
#     # именно так создали таблицу
#     # тут передается некое ключевое слово чтобы создать таблицу если такого таблицу не сущ
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), password  varchar(50))')
#     conn.commit() # синхронизирует изменение тоесть именно этой командой мы сохраняем все изменение
#     cur.close() # закрываем соединение с базой данных а также с файлом и курсором
#     conn.close()
#     # тут лежит соббщение которое будет выводиться после отправки команды /start
#     bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
#     # а тут мы уже запускаем следующую функцию чтобы совершить какие то последствие
#     bot.register_next_step_handler(message, user_name)

# def user_name(message):
#     global name
#     name = message.text.strip() # получили имя пользователья и записали в переменной name
#     bot.send_message(message.chat.id, 'Введите пароль') # и тут мы просим пользователья сразу ввести пароль 
#     bot.register_next_step_handler(message, user_password) # и далее переключаемся следующей функции

# def user_password(message): # это функция записывает данные пользователья в файл
#     password = message.text.strip() # пароль записываем в новую переменную не забываем метод стрип чтобы убрать лишние пробелы
#     conn = sqlite3.connect('itproger_telegram.sql') # тут мы снова подключаемся к базу данных чтобы записать имя и пароль пользователья
#     cur = conn.cursor()
#                 # тут мы как раз так и выставляем значение на нужное место
#     cur.execute(f"INSERT INTO users (name, password) VALUES ('{name}','{password}')")
#     conn.commit() # сохраняем 
#     cur.close()
#     conn.close()

#     # создаем кнопку которое будет выводится в конце и говорить не нужнали список юзеров 
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: True) # это декоратор обрабатывает работу кнопки тоесть что будет происходить при нажатии этой кнопки
# def callback(call):
#     conn = sqlite3.connect('itproger_telegram.sql')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall() # в этой переменной будет храниться все найденные записи от user тоесть это продолжение верхнего кода

#     info = ''
#     for i in users: # мы перебираем некий наш список состоящий из айди имя и пароль 
#         info += f"имя: {i[1]}, пароль: {i[-1]}\n"  # сохраняем немного отформатированный список
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info) # результат выполнение кнопки markup



"=====================LESSON 3====================="
# # этот код создает список из сообщении которые будут отправляться боту при нажатии
# @bot.message_handler(commands=['start'])
# def start(message):
#     # types.ReplyKeyboardMarkup() - это функция создает блочную кнопку
#     makrup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('перейти в macers 😍')
#     makrup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     makrup.row(btn2, btn3)
#     # по желании можно и отправить видео, фото, аудио и т.д
#     image = open('/home/hello/Downloads/1697994106588.jpg', 'rb')
#     bot.send_photo(message.chat.id, image, reply_markup=makrup)
#     # bot.send_message(message.chat.id, 'hello', reply_markup=makrup)
#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == 'перейти в macers':
#         bot.send_message(message.chat.id, 'website macers')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'delete')



# # content_types - обрабатывает какой тип сообщение отправил пользователь и на этом можно обработать такой случай и можно указать несколько тип данных
# # reply_makrup - добавляет определенную кнопку 
# # types.InlineKeyboardMarkup() - cоздает кнопку но внутри скобки должны указать такое слово как  types.InlineKeyboardButton("тут мы передаем сообщение которое будет отоброжаться", есть ещё многие параметры)
# # row - добавляет кнопки один или несколько 
# @bot.message_handler(content_types=['photo', 'audio'])
# def get_photo(message):
#     makrup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('перейти в macers', url='https://makers.courses/ide/python')
#     makrup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     makrup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото!', reply_markup=makrup)


# # это декоратор будет обрабатывать наши кнопки тоесть выполнять какое то действие
# # delete_message - удаляет некое сообщение он принимает два параметра (сам чат в котором мы работаем, далее айди сообщение которого он удалит и в айди хранится идентификатор сообщение по умолчанию он хранит свой а чтобы удалить предыдущий передаем -1)
# # edit_message_text - редактирует сообщение, и принимает три параметра (сообщение на которого он отредактирует, айди чата, и айди сообщение )
# @bot.callback_query_handler(func=lambda collback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id )






"========================LESSON 2===================="
# # commands - создает команды которые вводит пользователь через слеш


# @bot.message_handler(commands=['website'])
# def site(message):
#     # с помощью библиотеки и ключевого слово open нас переключает в сайт указанный в кобке нужно передавать строку
#     webbrowser.open('https://makers.courses/ide/python')


# # команда 
# @bot.message_handler(commands=['start', 'hello']) # можно добавить несколько команд на одну функцию # чтобы бот принял эти команды нужно прописывать в начале слеш
# # это функция будет запускаться каждый раз когда пользователь будет нажимать на кнопку старт
# # message - он будет хранить в себе всю всю информацию про пользователья и его айди
# def main(message):
#     # здесь мы обращаемся к нашему токену и говорим так чтобы он отправлял это сообщение при нажатии на кнопку старт
#     # в функции мы принимаем как раз так и соббщение тоесть там хранится какие то его данные 
#     # и через этот сообщение мы отправляем ему сообщение указывая его айди
#     # внутри нашего message хранится славарь мы можем вывести эти данные обращаясь по ключю
#     bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')




# # одна функция отвечает только за одну команду прописанного выше ного
# @bot.message_handler(commands=['help']) # не обходимо чтобы команду передать в списке
# def main(message):
#     bot.send_message(message.chat.id, '<i>Что нетак</i>?', parse_mode='html') # можно передавать html- свойства или стили преобразовывать какие то тексты и тагдалее

# # еще одна функция можно добавлять стикеры(эмодзи) в чат просто скопировали и вставили
# # создаем пустую кнопку благодарья которой мы можем не прписывать слеш
# @bot.message_handler()
# def info(message):
#     # конечно куда без проверки проверку совершаем внутри функции
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} 😍')
#     elif message.text.lower() == 'id':
#         # reply_to - отвечает на наше отправленное сообщение 
#         bot.reply_to(message, f'ID: {message.from_user.id}')
# # такую команду всегда нужно ставить в конец чтобы все функции должны были обрабатываемыми

# bot.polling(none_stop=True) # этот код запускают чтобы наш бот работал бесконечно и если его не запустить то бот не будет работать