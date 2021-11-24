from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from telegramBot.models.mixins import TimestampMixin
from telegramBot.models.database import Base

from telegramBot.models.users_words import users_words_table


class User(Base, TimestampMixin):
    name = Column(String(64), nullable=False, unique=True)
    user_word = relationship("Word", secondary=users_words_table, back_populates="user")
