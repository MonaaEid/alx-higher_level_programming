#!/usr/bin/python3


""" City Model"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
# engine = create_engine("sqlite:///:memory:")
# Base = declarative_base()


class City(Base):
    """ class State"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # Base.metadata.create_all(engine)
