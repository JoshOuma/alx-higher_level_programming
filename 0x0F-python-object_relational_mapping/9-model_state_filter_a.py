#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine=create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    states = session.query(State).filter(State.name.contains('a')).order_by(State.id.asc())

    # Printing states
    for state in states:
        print("{}: {}".format(state.id, state.name))