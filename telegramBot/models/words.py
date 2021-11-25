from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from telegramBot.models.database import Base
from telegramBot.models.mixins import TimestampMixin


class Word(Base, TimestampMixin):
    word = Column(String(120), nullable=False)
    translation = Column(String(120), nullable=False)

    user = relationship("AssociationTable", back_populates="word")
