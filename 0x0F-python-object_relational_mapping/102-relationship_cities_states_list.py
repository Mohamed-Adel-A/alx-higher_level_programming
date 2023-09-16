#!/usr/bin/python3
"""
a script that lists all City objects
from the database hbtn_0e_101_usa
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

    # query
    query_data = (session.query(State)
                  .order_by(State.id)
                  .all())

    for row in query_data:
        for city in row.cities:
            print("{}: {} -> {}".format(city.id, city.name, row.name))

    session.close()
