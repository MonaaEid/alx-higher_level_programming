#!/usr/bin/python3


""" State Model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
engine = create_engine("sqlite:///:memory:")
Base = declarative_base()


class State(Base):
    """ class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    Base.metadata.create_all(engine)
