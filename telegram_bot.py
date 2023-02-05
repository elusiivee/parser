import telebot
from telebot import types
# from telebot.service_utils import quick_markup


# from api_parsing import Link, LinkCar

# TODO dynamcially
AVAILABLE_CARS = {
    "Mercedes-Benz": 6,
    "Skoda": 24,
    "Ford": 48,
    "Audi": 70,
}

"""

1. Auto ID - не выводить, его нужно сохранять в а
2. 
3.
4.
5.

"""
car_brands = {'Alfa Romeo': 3, 'Audi': 6, 'BMW': 9, 'Bugatti': 109, 'Cadillac': 11, 'Chevrolet': 13, 'Citroen': 15,
              'Dodge': 118,
              'Ferrari': 22, 'Fiat': 23, 'Ford': 24, 'Honda': 28, 'Hyundai': 29, 'Jaguar': 31, 'Jeep': 32, 'Kia': 33,
              'Lada': 5553, 'Land Rover': 37, 'Lexus': 38, 'Maserati': 45, 'Maybach': 46, 'Mazda': 47,
              'Mercedes-Benz': 48,
              'Nissan': 55, 'Opel': 56, 'Porsche': 59, 'Skoda': 70, 'Smart': 71, 'Subaru': 75, 'Suzuki': 76,
              'Tesla': 2233,
              'Toyota': 79, 'Volvo': 85, 'Богдан': 188, 'ГАЗ': 91, 'ЗИЛ': 168, 'УАЗ': 93}


bot = telebot.TeleBot('5907984378:AAE1sael-9-4RqM-3KBecGZamRyfZIW3ic0')


@bot.message_handler(commands=['start'])  # two button (auto ria, find a car# )
def start(message):
    mess = f'Hi {message.from_user.first_name}, Let\'s get started \nChoose your option'
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('AutoRia')
    find_car = types.KeyboardButton('Find your car')
    markup.add(website, find_car)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(regexp='AutoRia')  # send AutoRia link
def AutoriaLink(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Link', url='https://auto.ria.com/'))
    bot.send_message(message.chat.id, 'Link to AutoRia', reply_markup=markup)


@bot.message_handler(regexp='Find your car')  # find our car
def choose_category(message):  # only passenger cars
    markup = types.ReplyKeyboardMarkup()
    category = types.KeyboardButton('passenger cars')
    markup.add(category)
    bot.send_message(message.chat.id, 'Choose the category', reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def callback(call: types.CallbackQuery):
    print(call.message.text)
    if call.message.text in car_brands.keys():   #call.data
        bot.send_message(call.message.chat.id, f'your choose is {call.data}',)


#TODO dinamekaly key size
@bot.message_handler(regexp='passenger cars')  # choose brand
def Set_brand(message):  # save brand to variable and convert it into id of car
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    # here has to be for loop
    for i, (key, val) in enumerate(car_brands.items()):
        markup.add(types.InlineKeyboardButton(key, callback_data=val))
    bot.send_message(message.chat.id, 'Choose the brand', reply_markup=markup)
    
    # userbrand = message.text
    # all_cars = [sub['name'] for sub in car_brands]
    # id_car = all_cars.index(userbrand)
    # all_values = [sub['value'] for sub in car_brands]
    # id_values = all_values[id_car]
    # bot.send_message(message.chat.id, id_values)
    # # Link._middle_url=message.text



    #************************
    # markup = types.InlineKeyboardMarkup()
    # for key, value in car_brands.items():
    #     markup.add(types.InlineKeyboardButton(text=key,
    #                                           callback_data=key))
    # bot.send_message(message.chat.id, 'Choose the brand', reply_markup=markup)

    # ************************



# @bot.message_handler(content_types=['text'])
# def after_text(message):
#     markup=types.ReplyKeyboardMarkup()
#     item=types.KeyboardButton("Mercedes")
#     if message.text == 1:
#         bot.send_message(message.from_user.id, 'Enter phone number:')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'use: /start to start the program')


@bot.message_handler()
def any_message(message):
    bot.send_message(message.chat.id, 'use: /help')


bot.polling(none_stop=True)


'1) set to the Cat.category.id = 1 while we have only pasanger cars' \
'2) get the id of car brand and set to the Car.' \
'3) firstly output all id of our car and then user should'