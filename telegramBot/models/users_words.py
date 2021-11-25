from sqlalchemy import Table, Column, Integer, ForeignKey

from telegramBot.models.database import Base
from telegramBot.models.mixins import TimestampMixin
from sqlalchemy.orm import relationship

#
# users_words_table = Table(
#     "bot_users_words_association_table",
#     Base.metadata,
#     Column("word_id", Integer, ForeignKey("bot_words.id"), primary_key=True),
#     Column("user_id", Integer, ForeignKey("bot_users.id"), primary_key=True),
# )


class AssociationTable(Base, TimestampMixin):
    word_id = Column(ForeignKey('bot_words.id'), primary_key=True)
    user_id = Column(ForeignKey('bot_users.id'), primary_key=True)
    word = relationship('Word', back_populates='user')
    user = relationship('User', back_populates='word')
