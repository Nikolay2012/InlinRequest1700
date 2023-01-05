'''
    Модуль який додає клавіатуру для кнопки get_picture
'''
import telebot
import modules.button_get_picture as m_bt_picture 

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.add(m_bt_picture.button)

