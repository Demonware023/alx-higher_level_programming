#!/usr/bin/python3
"""Script to change the name of a State object from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine that connects to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Check if the State object exists
    if state:
        # Change the name of the State object to "New Mexico"
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()
