import logging
from pprint import pprint
from random import randint


from telegram_bot.models.database import Session
from telegram_bot.models.user import User
from telegram_bot.models.words import Word
from telegram_bot.models.users_words import AssociationTable
from telegram_bot.usecase.database_functions import get_user, get_word, get_user_words
from telegram_bot.usecase.translation_requests import complete_word


def add_new_user(user_id: int, name: str):
    try:
        with Session() as s:
            user = s.query(User).filter_by(user_id=user_id).first()
            if user:
                logging.warning('User exists')
            else:
                user = User(user_id=user_id, name=name)
                s.add(user)
                s.commit()
    except Exception:
        logging.warning('User exists')


def add_new_word(word: str, user_id: int):
    user = get_user(user_id)
    if get_word(word):
        return
    new_word = complete_word(word)
    word_to_add = Word(word=new_word.word, translation=new_word.translation)
    with Session() as s:
        association = AssociationTable(id=0, word=word_to_add, user=user)
        s.add(association)
        s.commit()
        return association.word


def request_random_word(user_id: int):
    words = get_user_words(user_id)
    try:
        rnd = randint(0, len(words)-1)
    except Exception:
        logging.warning('No words added')
        return
    return words[rnd]
