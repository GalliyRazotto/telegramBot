import logging
from telegramBot.models.database import Session
from telegramBot.models.user import User
from telegramBot.models.words import Word
from telegramBot.models.users_words import AssociationTable
from telegramBot.usecase.translation_requests import complete_word


def add_new_user(telegram_nickname):
    with Session() as s:
        user = s.query(User).filter_by(name=telegram_nickname).first()
        if user:
            logging.warning('User already added')
        else:
            user = User(name=telegram_nickname)
            s.add(user)
            s.commit()


def get_user_id(user_name: str):
    with Session() as s:
        user = s.query(User).filter_by(name=user_name).first()
        return user.id


def get_word_id(word: str):
    with Session() as s:
        res = s.query(Word).filter_by(word=word).first()
        return res.id


def add_new_word(word: str, user_name: str):
    with Session() as s:
        if s.query(Word).filter_by(word=word.lower()).first():
            s.close()
            return False
        else:
            new_word = complete_word(word)
            word_to_add = Word(word=new_word.word, translation=new_word.translation)
            s.add(word_to_add)
            s.commit()
            association = AssociationTable(id=0, word_id=word_to_add.id, user_id=get_user_id(user_name))
            s.add(association)
            s.commit()
            return True


if __name__ == '__main__':
    add_new_word('Hype', 'Kirill🚯')
