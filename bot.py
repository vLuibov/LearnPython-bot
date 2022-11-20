import logging      # запись отчета о работе бота
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters    # Updater коммуницирует с сервером Телеграма, CommandHandler - обработка команд, MessageHandler - обработка сообщений пользователя, Filters - библиотека

import settings # скрыть ключ в файл 

logging.basicConfig(filename='bot.log', level=logging.INFO) # запись о работе в файл .log, уровни важности

def greet_user(update, context): # ответ на /start
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь Telegram!') # ответ пользователю
    print(update)               # информация о пользователе

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)    

def main():                         # основной код
    mybot = Updater(settings.API_KEY, use_context=True)  # передать ключ от бота
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) # обработка команды /start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) #  после приветствия, чтобы не перехватить его, Filters.text - только текст

    logging.info("Bot started")     # запись в лог
    mybot.start_polling()           # обращение за обновлениями
    mybot.idle()                    # постоянная работа, бесконечный цикл

if __name__ == "__main__":
    main()                          # безопасный вызов функции 