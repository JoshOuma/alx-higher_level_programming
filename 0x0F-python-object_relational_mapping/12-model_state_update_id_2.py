#!/usr/bin/python3
"""
Updates the name of a State object from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_id = 2  # Replace with the desired State ID
    new_state_name = "New Mexico"  # Replace with the desired new state name

    # Create an engine to connect to the MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the specified ID
    queried_state = session.query(State).filter_by(id=state_id).first()

    if queried_state:
        queried_state.name = new_state_name
        session.commit()
        print(f"State {state_id} updated to {new_state_name}")
    else:
        print(f"State with ID {state_id} not found")

    session.close()
