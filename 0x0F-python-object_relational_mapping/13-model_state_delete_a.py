#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    # Create a session
    session = Session(engine)

    # Query for all states containing 'a' in their name
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()
    session.close()
