#!/usr/bin/python3
"""
Lists all states objects from the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine, select
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """SQLAlchemy database engine created with pooling & pre-ping"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True,
    )
    """Establish connection to the database"""
    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        first_state = connection.execute(query).fetchone()

        """Iterate over results & display them"""
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

    engine.dispose()
