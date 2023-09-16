#!/usr/bin/python3
"""
a script that prints the State object
with the name passed as argument
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

    # query
    state_name = sys.arg[4]
    query_data = (session.query(State)
                  .filter(State.name == state_name)
                  .first())

    # print
    if query_data is None:
        print("Not found")
    else:
        print(query_data.id)

    session.close()
