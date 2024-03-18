#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
