from dataclasses import dataclass
import googletrans


@dataclass
class Word:
    word: str
    translation: str


def word_translation(word: str):
    translator = googletrans.Translator()

    # TODO аккуратней будет так:
    destination = 'ru'
    if "en" not in translator.detect(word).lang:
        destination = 'en'

    try:
        translation = translator.translate(word, dest=destination).text
        return translation
    except Exception:
        # TODO Вместо принтов используй модуль logging
        print('Something goes wrong')


def complete_word(word: str):
    new_word = Word(word=word, translation=word_translation(word))
    return new_word


if __name__ == '__main__':
    complete_word('заложник')
