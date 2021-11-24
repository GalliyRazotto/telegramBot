from telegramBot.models.database import Session
from telegramBot.models.user import User
from telegramBot.models.words import Word
from telegramBot.usecase.translation_requests import complete_word


def add_new_user(telegram_nickname):
    # TODO тут и в подобных случаях, я бы использовал with
    session = Session()
    # TODO
    #  т.е. ты ищешь пользователя. и если нашёл ок. а если не нашёл то разве first не вернёт None?
    #  и тогда session.add(user) фактически session.add(None)
    #  И мб эту проверку доверить SQL name для пользователя всё равно уникально.
    #  И если попробуешь добавить существуещего пользователя, то получишь исключение
    user = session.query(User).filter_by(name=telegram_nickname).first()
    if user:
        print('User already added')
    else:
        session.add(user)
        session.commit()
        session.close()


def get_user_id(user_name: str):
    session = Session()
    user = session.query(User).filter_by(name=user_name).first()
    session.close()
    # TODO а если не найдёт и вернёт None?
    return user.id


def add_new_word(word: str, user_name: str):
    session = Session()
    if session.query(Word).filter_by(word=word.lower()).first():
        session.close()
        return False
    else:
        new_word = complete_word(word)
        word_to_add = Word(word=new_word.word, translation=new_word.translation, user_id=get_user_id(user_name))
        session.add(word_to_add)
        session.commit()
        session.close()
        return True


if __name__ == '__main__':
    add_new_word('Hype', 'Kirill🚯')
