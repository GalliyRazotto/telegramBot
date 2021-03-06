from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr


class Base:
    __mapper_args__ = {"eager_defaults": True}

    @declared_attr
    def __tablename__(cls):
        return f"bot_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


engine = create_engine("postgresql://user:password@localhost:5432/telegram_bot", echo=True)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

