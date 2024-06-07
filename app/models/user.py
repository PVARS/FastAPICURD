from sqlalchemy import Column, Integer, String
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String(100))
    last_name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=True)
    user_name = Column(String(50), unique=True)
    gender = Column(Integer)
