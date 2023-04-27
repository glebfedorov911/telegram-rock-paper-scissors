import telebot
import random

token = '6052576965:AAEbG15-cnl6zFXGK9MrbTcKLB8c17dF5Go'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = f"Привет, {message.from_user.username}, для игры напиши /game"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['game'])
def game(message):
    mark_up = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = [telebot.types.KeyboardButton('Камень'),
            telebot.types.KeyboardButton('Ножницы'),
            telebot.types.KeyboardButton('Бумага')]
    for i in item:
        mark_up.add(i)

    bot.send_message(message.chat.id, 'Начинай!', reply_markup=mark_up)


@bot.message_handler(content_types='text')
def messages(message):
    sockgame = {'Бумага':'Камень', 'Камень':'Ножницы', 'Ножницы':'Бумага'}
    sockgame_list = ['Бумага', 'Камень', 'Ножницы']
    sock_check = random.randint(0, 2)
    if message.text in sockgame:
        a = sockgame[sockgame_list[sock_check]]
        bot.send_message(message.chat.id, a)
        if sockgame[message.text] == a:
            bot.send_message(message.chat.id, 'Ты выиграл')
        elif message.text == a:
            bot.send_message(message.chat.id, 'Ничья')
        elif sockgame[a] == message.text:
            bot.send_message(message.chat.id, 'Ты проиграл')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю =(')

bot.infinity_polling()