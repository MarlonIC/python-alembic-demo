from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Unicode(200), nullable=True)
