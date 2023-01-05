'''
    Створюємо кнопки для обратного зв'язку з ботом
'''
import telebot 
inline_button1 = telebot.types.InlineKeyboardButton(text= 'Замовити', callback_data= 'замовити')
inline_button2 = telebot.types.InlineKeyboardButton(text= 'Перейти до магазину', url="https://www.apple.com/ua/iphone/")