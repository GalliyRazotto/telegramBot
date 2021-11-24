from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from telegramBot.models.users_words import users_words_table

from telegramBot.models.database import Base
from telegramBot.models.mixins import TimestampMixin


class Word(Base, TimestampMixin):
    __table_args__ = {'extend_existing': True},

    word = Column(String(120), nullable=False)
    translation = Column(String(120), nullable=False)

    user_id = Column(Integer, ForeignKey('bot_users.id'))
    user = relationship("User", secondary=users_words_table, back_populates="user_word")
