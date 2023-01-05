'''
    Клавіатура для додавання кнопок зворотнього зв'язку
'''

import telebot 
import modules.create_inline_button as m_inline_button
inline_keyboard = telebot.types.InlineKeyboardMarkup()
inline_keyboard.add(m_inline_button.inline_button1, m_inline_button.inline_button2)
