#!/usr/bin/python3
"""
a script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    # create an engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(db_user, db_passwd, db_name),
                           pool_pre_ping=True)

    # generate database schema
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()

    # add new state and new city
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
