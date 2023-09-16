#!/usr/bin/python3
"""
a script that prints all City objects
from the database hbtn_0e_14_usa:
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

    # delete state with letter a
    query_data = (session.query(State, City)
                  .filter(State.id == City.state_id)
                  .all())

    for row in query_data:
        print(row)

    session.commit()
    session.close()
