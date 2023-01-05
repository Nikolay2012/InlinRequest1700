'''
    Модуль який відправляє повідомлення користувачеві
'''
import modules.create_bot as m_bot
import modules.search_path_to_file as m_search_path
import modules.create_inline_keyboard as m_inline_keyboard

def send_picture(message):
    if message.text.lower() == "get picture":
        file_path = m_search_path.path_file("images/1.jpeg")
        m_bot.bot.send_photo(
            message.chat.id,
            open(file_path, "rb"),
            "Iphone 14",
            reply_markup= m_inline_keyboard.inline_keyboard
        )
        
    m_bot.bot.register_next_step_handler(message,send_picture)