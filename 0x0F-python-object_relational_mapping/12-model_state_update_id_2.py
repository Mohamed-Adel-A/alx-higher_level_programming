#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


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

    # update state
    query_data = (session.query(State)
                  .filter(State.id == 2)
                  .first())

    if query_data is not None:
        query_data.name = "New Mexico"
        session.commit()

    session.close()
