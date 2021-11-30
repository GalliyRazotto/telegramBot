# telegramTranslationWordBot
TelegramBot - бот для изучения слов английского языка.
В перспективе сделать следующие функции:
 - добавление новых слов и их синонимов в словарь
 - изучение добавленных слов (бот случайно выдает слово и предлагает несколько вариантов перевода для выбора)
 - предложение изучения добавленных слов
 - предложение статей для прочтения с упоминанием добавленных слов
 - 
На данный момент работает:
 - перевод слова
 - добавлене новых слов в словарь
 - запрос случайного слова с необходимостью дать ответ

Словарь для всех пользователей один. Слава и пользователи связаны Many To Many.

Запускаем бота:
 - добавляем в телеграме бота BotFather. С его помощью создаем своего бота, следуя инструкции, предложенной botFather. На выходе нам нужно получить TOKEN и определить команды, которые в будущем будут использованы в нашем приложении. В данном случае - это команды /start, /add, /request, /translate
 - TOKEN - токен, сгенерированный botFather, добавляем в переменную окружения
 - устанавливаем зависимости pip install -r requirements.txt
 - запускаем docker-compose up -d
 - делаем миграции alembic upgrade head
 - запускаем логику приложения - Main.py
 - для подключения к БД используем лубое удобное для вас приложение. В моем случае - это dbeaver

После первого добавления бота доступна одна кнопка Start - добавление нового пользователя в БД
