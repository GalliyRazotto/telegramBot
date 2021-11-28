from sqlalchemy import Column, ForeignKey
from telegram_bot.models.mixins import TimestampMixin

from telegram_bot.models.database import Base
from sqlalchemy.orm import relationship


class AssociationTable(Base, TimestampMixin):
    word_id = Column(ForeignKey('bot_words.id'), primary_key=True)
    user_id = Column(ForeignKey('bot_users.id'), primary_key=True)
    word = relationship('Word', back_populates='user')
    user = relationship('User', back_populates='word')
