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
        s.close()


def get_user_id(user_name: str):
    with Session() as s:
        user = s.query(User).filter_by(name=user_name).first()
        s.close()
        if user:
            return user.id
        else:
            return 'User not found'


def get_word_id(word: str):
    with Session() as s:
        res = s.query(Word).filter_by(word=word).first()
        s.close()
        if res:
            return res.id
        else:
            return 'Word not found'


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
            s.close()
            with Session() as ses:
                association = AssociationTable(word_id=word_to_add.id, user_id=get_user_id(user_name))
                ses.add(association)
                ses.commit()
                ses.close()
            return True


if __name__ == '__main__':
    add_new_word('Hype', 'Kirill🚯')
    # add_new_user('Ivan')
