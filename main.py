'''
    Модуль в якому ми приєднуємо всі модулі та активує роботу проекту
'''
import modules.create_bot as m_bot
import modules.command_start as m_start
import modules.processing_request as m_processing_request



m_bot.bot.polling(none_stop= True)