import telebot
from telebot import types
from bs4 import BeautifulSoup as b
import random
import requests
from settings import TG_TOKEN,TG_API_URL

URL = 'https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=100-700.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    otels = soup.find_all('h2', class_='zen-hotelcard-name')
    return [c.text for c in otels]
list_of_otels = parser(URL)
random.shuffle(list_of_otels)




bot = telebot.TeleBot('5889153821:AAFsKhFpNr12wsa6vEblb3nacR5t7bQJIXs')


@bot.message_handler(commands=['start'])
def start(message):
    mess_1 = f'Привет,<b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id,mess_1, parse_mode='html')
    markup_1 = types.InlineKeyboardMarkup()
    zvezda_1 = types.InlineKeyboardButton(text="★",
    callback_data="NumberOne")
    zvezda_2 = types.InlineKeyboardButton(text="★★",
    callback_data="NumberTwo")
    zvezda_3 = types.InlineKeyboardButton(text="★★★",
    callback_data="NumberTree")
    zvezda_4 = types.InlineKeyboardButton(text="★★★★",
    callback_data="Numberfour")
    zvezda_5 = types.InlineKeyboardButton(text="★★★★★",
    callback_data="Numberfive")
    markup_1.add(zvezda_1, zvezda_2, zvezda_3, zvezda_4, zvezda_5)
    bot.send_message(message.chat.id, 'Это бот, который подбирает отели в Москве.' '\n' '\n' 'От самых дешевых -> до самых дорогих' '\n''\n' 'Выберите колличество звезд отеля: 😁''\n' '\n' '❗От колличества звезд зависит цена проживания❗', reply_markup=markup_1)


@bot.callback_query_handler(func=lambda c:True)
def inlin(c):

    if c.data == 'NumberOne':

        markup_1 = types.InlineKeyboardMarkup()
        pay_1 = types.InlineKeyboardButton(text="0-700₽",
        callback_data="PAY_1_1")
        pay_2 = types.InlineKeyboardButton(text="701₽-900₽",
        callback_data="PAY_1_2")
        pay_3 = types.InlineKeyboardButton(text="901₽-1200₽",
        callback_data="PAY_1_3")
        pay_4 = types.InlineKeyboardButton(text="1201₽-1400₽",
        callback_data="PAY_1_4")
        pay_5 = types.InlineKeyboardButton(text="1401₽-1600₽",
        callback_data="PAY_1_5")
        markup_1.add(pay_1,pay_2,pay_3,pay_4,pay_5)
        bot.send_message(c.message.chat.id, 'Выбери ценовой диапозон:',reply_markup=markup_1)


    if c.data == 'PAY_1_1':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=100-700.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_1")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn)

    if c.data == 'obnovit_1_1':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=100-700.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_1")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn)


    if c.data == 'PAY_1_2':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=700-900.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_2")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn)

    if c.data == 'obnovit_1_2':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=700-900.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
                                               callback_data="obnovit_1_2")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn)


    if c.data == 'PAY_1_3':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=900-1200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_3")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn)

    if c.data == 'obnovit_1_3':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=900-1200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
                                               callback_data="obnovit_1_3")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn)


    if c.data == 'PAY_1_4':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1200-1400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_4")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn)

    if c.data == 'obnovit_1_4':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1200-1400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
                                               callback_data="obnovit_1_4")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn)


    if c.data == 'PAY_1_5':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
                                                url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1400-1600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_5")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn)

    if c.data == 'obnovit_1_5':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1400-1600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_1_5")
        markup_obn.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn)


    if c.data == 'NumberTwo':

        markup_2 = types.InlineKeyboardMarkup()
        pay_1_2 = types.InlineKeyboardButton(text="1600-1800₽",
        callback_data="PAY_2_1")
        pay_2_2 = types.InlineKeyboardButton(text="1800-2000₽",
        callback_data="PAY_2_2")
        pay_3_2 = types.InlineKeyboardButton(text="2000-2200₽",
        callback_data="PAY_2_3")
        pay_4_2 = types.InlineKeyboardButton(text="2200-2400₽",
        callback_data="PAY_2_4")
        pay_5_2 = types.InlineKeyboardButton(text="2400-2600₽",
        callback_data="PAY_2_5")
        markup_2.add(pay_1_2,pay_2_2,pay_3_2,pay_4_2,pay_5_2)
        bot.send_message(c.message.chat.id, 'Выбери ценовой диапозон:',reply_markup=markup_2)

    if c.data == 'PAY_2_1':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1600-1800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_1")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_2_1':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1600-1800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_1")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_2_2':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1800-2000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_2")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_2_2':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=1800-2000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_2")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_2_3':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2000-2200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_3")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_2_3':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2000-2200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_3")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_2_4':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2200-2400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_4")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_2_4':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2200-2400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_4")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_2_5':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2400-2600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_5")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_2_5':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2400-2600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_2_5")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'NumberTree':

        markup_3 = types.InlineKeyboardMarkup()
        pay_1_2 = types.InlineKeyboardButton(text="2600-2800₽",
        callback_data="PAY_2_1")
        pay_2_2 = types.InlineKeyboardButton(text="2800-3000₽",
        callback_data="PAY_2_2")
        pay_3_2 = types.InlineKeyboardButton(text="3000-3200₽",
        callback_data="PAY_2_3")
        pay_4_2 = types.InlineKeyboardButton(text="3200-3400₽",
        callback_data="PAY_2_4")
        pay_5_2 = types.InlineKeyboardButton(text="3400-3600₽",
        callback_data="PAY_2_5")
        markup_3.add(pay_1_2,pay_2_2,pay_3_2,pay_4_2,pay_5_2)
        bot.send_message(c.message.chat.id, 'Выбери ценовой диапозон:',reply_markup=markup_3)


    if c.data == 'PAY_3_1':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_3 = types.InlineKeyboardMarkup()
        markup_3.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2600-2800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_3)

        markup_obn_3 = types.InlineKeyboardMarkup()
        obn_3 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_1")
        markup_obn_3.add(obn_3)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_3)


    if c.data == 'obnovit_3_1':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_3 = types.InlineKeyboardMarkup()
        markup_3.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2600-2800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_3)

        markup_obn_3 = types.InlineKeyboardMarkup()
        obn_3_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_1")
        markup_obn_3.add(obn_3_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_3)


    if c.data == 'PAY_3_2':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_3_2 = types.InlineKeyboardMarkup()
        markup_3_2.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2800-3000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_3_2)

        markup_obn_3_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_2")
        markup_obn_3_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_3_2)


    if c.data == 'obnovit_3_2':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=2800-3000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_3_2 = types.InlineKeyboardMarkup()
        obn_3_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_2")
        markup_obn_3_2.add(obn_3_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_3_2)


    if c.data == 'PAY_3_3':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3000-3200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_3")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_3_3':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3000-3200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_3")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_3_4':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3200-3400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_4")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_3_4':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3200-3400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_4")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_3_5':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3400-3600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_5")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_3_5':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3400-3600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_3_5")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)



    if c.data == 'Numberfour':

        markup_4 = types.InlineKeyboardMarkup()
        pay_1_2 = types.InlineKeyboardButton(text="3600-3800₽",
        callback_data="PAY_2_1")
        pay_2_2 = types.InlineKeyboardButton(text="3800-4000₽",
        callback_data="PAY_2_2")
        pay_3_2 = types.InlineKeyboardButton(text="4000-4200₽",
        callback_data="PAY_2_3")
        pay_4_2 = types.InlineKeyboardButton(text="4200-4400₽",
        callback_data="PAY_2_4")
        pay_5_2 = types.InlineKeyboardButton(text="4400-4600₽",
        callback_data="PAY_2_5")
        markup_4.add(pay_1_2,pay_2_2,pay_3_2,pay_4_2,pay_5_2)
        bot.send_message(c.message.chat.id, 'Выбери ценовой диапозон:',reply_markup=markup_4)


    if c.data == 'PAY_4_1':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3600-3800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_1")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_4_1':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3600-3800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_1")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_4_2':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3800-4000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_2")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_4_2':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=3800-4000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_2")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_4_3':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4000-4200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_3")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_4_3':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4000-4200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_3")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_4_4':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4200-4400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_4")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_4_4':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4200-4400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_4")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_4_5':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4400-4600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_5")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_4_5':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4400-4600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_4_5")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)



    if c.data == 'Numberfive':

        markup_5 = types.InlineKeyboardMarkup()
        pay_1_2 = types.InlineKeyboardButton(text="4600-4800₽",
        callback_data="PAY_2_1")
        pay_2_2 = types.InlineKeyboardButton(text="4800-5000₽",
        callback_data="PAY_2_2")
        pay_3_2 = types.InlineKeyboardButton(text="5000-5200₽",
        callback_data="PAY_2_3")
        pay_4_2 = types.InlineKeyboardButton(text="5200-5400₽",
        callback_data="PAY_2_4")
        pay_5_2 = types.InlineKeyboardButton(text="5400-5600₽",
        callback_data="PAY_2_5")
        markup_5.add(pay_1_2,pay_2_2,pay_3_2,pay_4_2,pay_5_2)
        bot.send_message(c.message.chat.id, 'Выбери ценовой диапозон:',reply_markup=markup_5)


    if c.data == 'PAY_5_1':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4600-4800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_1")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_5_1':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4600-4800.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_1")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_5_2':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4800-5000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_2")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_5_2':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=4800-5000.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_2")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_5_3':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5000-5200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_3")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_5_3':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5000-5200.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_3")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_5_4':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5200-5400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_4")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_5_4':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5200-5400.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_4")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)


    if c.data == 'PAY_5_5':

        mess_1_1 = '😉 Наши предложения: 😉'

        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5400-5600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_1 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_5")
        markup_obn_2.add(obn_1)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить отель: 💫', reply_markup=markup_obn_2)


    if c.data == 'obnovit_5_5':

        mess_1_1 = '😉 Наши предложения: 😉'
        bot.send_message(c.message.chat.id, mess_1_1, parse_mode='html')
        bot.send_message(c.message.chat.id, list_of_otels[0])
        del list_of_otels[0]

        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посетить веб сайт',
        url='https://ostrovok.ru/hotel/russia/moscow/?q=2395&guests=2&price=5400-5600.one&stars=0.1&sid=ae3b4e0b-f01c-405d-95c3-500ba9fd4418'))
        bot.send_message(c.message.chat.id, '----Перейдите на сайт----', reply_markup=markup_1)

        markup_obn_2 = types.InlineKeyboardMarkup()
        obn_2 = types.InlineKeyboardButton(text="Обновить",
        callback_data="obnovit_5_5")
        markup_obn_2.add(obn_2)
        bot.send_message(c.message.chat.id, '💫 Нажмите чтобы обновить список: 💫', reply_markup=markup_obn_2)



@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет" :
        bot.send_message(message.chat.id,'И тебе привет', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('icon1.png','rb')
        bot.send_photo(message.chat.id,photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')
        bot.send_message(message.chat.id, 'напиши /start', parse_mode='html')


# def main(bot):
#     bot = Updater(TG_TOKEN,TG_API_URL, use_context = True)


bot.polling()