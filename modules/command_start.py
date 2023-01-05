'''
    Модуль який перевіряє та обробляє комаду старт
'''
import modules.create_bot as m_bot 
import modules.send_message_user as m_message_user
import modules.create_keyboard_get_picture as m_key_get_picture

@m_bot.bot.message_handler(commands=['start'])
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id,
        "Hi!", 
        reply_markup= m_key_get_picture.keyboard 
    )
    m_bot.bot.register_next_step_handler(
        message, 
        m_message_user.send_picture   
    )