from pprint import pprint

from telegram_bot.models.database import Session
from telegram_bot.models.user import User
from telegram_bot.models.words import Word


def get_user(user_name: str):
    with Session() as s:
        user = s.query(User).filter_by(name=user_name).first()
        pprint(user)
        return user


def get_word(word: str):
    with Session() as s:
        res = s.query(Word).filter_by(word=word.lower()).first()
        return res


def get_user_words(user_name: str):
    with Session() as s:
        words = s.query(Word).join(User.word, Word).filter(User.name.ilike(user_name)).all()
        return words


if __name__ == '__main__':
    get_user_words('Kirill🚯')
