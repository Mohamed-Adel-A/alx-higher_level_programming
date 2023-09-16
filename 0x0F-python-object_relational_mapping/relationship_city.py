#!/usr/bin/python3
"""
contains the class definition of a City
"""
from relationship_state import Base 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    class definition of a City
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
