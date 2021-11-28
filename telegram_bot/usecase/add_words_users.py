import logging
from pprint import pprint
from random import randint


from telegram_bot.models.database import Session
from telegram_bot.models.user import User
from telegram_bot.models.words import Word
from telegram_bot.models.users_words import AssociationTable
from telegram_bot.usecase.database_functions import get_user, get_word, get_user_words
from telegram_bot.usecase.translation_requests import complete_word


def add_new_user(telegram_nickname: str):
    try:
        with Session() as s:
            user = s.query(User).filter_by(name=telegram_nickname).first()
            if user:
                logging.warning('User exists')
            else:
                user = User(name=telegram_nickname)
                s.add(user)
                s.commit()
    except Exception:
        logging.warning('User exists')


def add_new_word(word: str, user_name: str):
    user = get_user(user_name)
    if get_word(word):
        return
    new_word = complete_word(word)
    word_to_add = Word(word=new_word.word, translation=new_word.translation)
    with Session() as s:
        association = AssociationTable(id=0, word=word_to_add, user=user)
        s.add(association)
        s.commit()
        return word


def request_random_word(user_name: str):
    words = get_user_words(user_name)
    try:
        rnd = randint(0, len(words)-1)
    except Exception:
        logging.warning('No words added')
        return
    return words[rnd]


if __name__ == '__main__':
    # add_new_word('big', 'Kirill🚯')
    request_random_word('Kirill🚯')

