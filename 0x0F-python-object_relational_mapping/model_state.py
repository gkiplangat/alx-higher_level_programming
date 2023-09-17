#!/usr/bin/python3
"""Define a State class and create a connection to the database.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""Create an instance of declarative base"""
Base = declarative_base()


class State(Base):
    """Define the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
