from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from telegramBot.models.mixins import TimestampMixin
from telegramBot.models.database import Base


class User(Base, TimestampMixin):
    name = Column(String(64), nullable=False, unique=True)
    word = relationship("AssociationTable", back_populates="user")

