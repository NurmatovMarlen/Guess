import telebot
from decouple import config
from keyboards.inline_keyboard import inline_key_yes_no

bot = telebot.TeleBot(config('TOKEN'))


@bot.message_handler(commands=['play', ])
def welcome(message):
    msg = bot.send_message(message.chat.id, 'Welcome!')
    start_game(msg)


def start_game(message):
    bot.send_message(message.chat.id, 'Wanna play the game?', reply_markup=inline_key_yes_no)


@bot.callback_query_handler(func=lambda c: True)
def callback_inline(c):
    if c.data == 'yes':
        msg = bot.send_message(c.message.chat.id, 'choose any number between 1-10')
        bot.register_next_step_handler(msg, game)

    if c.data == 'no':
        bot.send_message(c.message.chat.id, 'bye')
        bot.send_sticker(c.message.chat.id, '1778287908:AAElpmhBnfrngdudGAup3sqbwFCz92iQqAg')


def game(message):
    import random
    num = int(random.randint(1, 11))
    print(num)
    tries = 3

    def game_body(message):
        guess = int(message.text)
        nonlocal tries
        if guess == num:
            bot.send_message(message.chat.id, 'Congratulations!')
            tries -= 1
            bot.send_message(message.chat.id, f'it took you {3 - tries} tries to find guessed number')
            start_game(message)
        elif tries == 1:
            bot.send_message(message.chat.id, 'You loose')
            start_game(message)
        elif guess > num:
            tries -= 1
            bot.send_message(message.chat.id, 'guess number is lower than you have typed')
            msg = bot.send_message(message.chat.id, f'you have {tries} tries left')
            bot.register_next_step_handler(msg, game_body)
        elif guess < num:
            tries -= 1
            bot.send_message(message.chat.id, 'guess number is higher than you have typed')
            msg = bot.send_message(message.chat.id, f'you have {tries} tries left')
            bot.register_next_step_handler(msg, game_body)

    game_body(message)


bot.polling(none_stop=True)