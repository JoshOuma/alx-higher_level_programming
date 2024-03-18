#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the specified name
    queried_state = session.query(State).filter_by(State.name == sys.argv[4]).first()

    if queried_state:
        print(f"{queried_state.id}: {queried_state.name}")
    else:
        print("Not found")
