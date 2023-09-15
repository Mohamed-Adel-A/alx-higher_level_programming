#!/usr/bin/python3
"""
contains the class definition of a State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    class definition of a State
    """
    __tablename__= "states"
    id = Column(Integer, primary_key=True, nuique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
