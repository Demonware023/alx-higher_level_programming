#!/usr/bin/python3
"""Script to print the id of the State object with the given name from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine that connects to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the given name
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Print the id of the State object if found, otherwise print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
