from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_key_yes_no = InlineKeyboardMarkup()
btn_yes = InlineKeyboardButton('Да', callback_data='yes')
btn_no = InlineKeyboardButton('Нет', callback_data='no')

inline_key_yes_no.add(btn_yes, btn_no)