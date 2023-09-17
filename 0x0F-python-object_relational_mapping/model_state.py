#!/usr/bin/python3
"""
   Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create the engine with a more readable format
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create the tables based on the models
    Base.metadata.create_all(engine)