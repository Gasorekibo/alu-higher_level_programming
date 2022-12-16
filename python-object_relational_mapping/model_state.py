#!/usr/bin/python3
"""
    python file that contains the class definition of a State
    and an instance
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        class city inherit from Base
        3 attributes:
        city's id
        city's name
        city's state name
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
