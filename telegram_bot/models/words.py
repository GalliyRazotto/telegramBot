from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from telegram_bot.models.database import Base
from telegram_bot.models.mixins import TimestampMixin


class Word(Base, TimestampMixin):
    word = Column(String(120), nullable=False)
    translation = Column(String(120), nullable=False)

    user = relationship("AssociationTable", back_populates="word")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"word={self.word!r}, translation={self.translation}, "
        )

    def __repr__(self):
        return str(self)
