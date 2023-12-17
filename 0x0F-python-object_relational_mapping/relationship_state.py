#!/usr/bin/python3


""" State Model"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import (create_engine)
# engine = create_engine("sqlite:///:memory:")
# Base = declarative_base()
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """ class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,  nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    # Base.metadata.create_all(engine)
    