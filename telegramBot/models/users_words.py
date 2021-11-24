from sqlalchemy import Table, Column, Integer, ForeignKey

from telegramBot.models.database import Base


users_words_table = Table(
    "bot_users_words_association_table",
    Base.metadata,
    Column("word_id", Integer, ForeignKey("bot_words.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("bot_users.id"), primary_key=True),
)
