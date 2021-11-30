from pprint import pprint

from telegram_bot.models.database import Session
from telegram_bot.models.user import User
from telegram_bot.models.words import Word


def get_user(user_id: int):
    with Session() as s:
        user = s.query(User).filter_by(user_id=user_id).first()
        pprint(user)
        return user


def get_word(word: str):
    with Session() as s:
        res = s.query(Word).filter_by(word=word.lower()).count()
        return res


def get_user_words(user_id: int):
    with Session() as s:
        words = s.query(Word).join(User.word, Word).filter(User.user_id.__eq__(user_id)).all()
        return words
