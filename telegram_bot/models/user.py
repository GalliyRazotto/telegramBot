from sqlalchemy import (
    Column,
    String,
    Integer,
)
from sqlalchemy.orm import relationship

from telegram_bot.models.mixins import TimestampMixin
from telegram_bot.models.database import Base


class User(Base, TimestampMixin):
    user_id = Column(Integer, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)
    word = relationship("AssociationTable", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}, word={self.word}, "
        )

    def __repr__(self):
        return str(self)
