#!/usr/bin/python3
"""Script to add the State object "Louisiana" to the database"""

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

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit changes to the database
    session.add(new_state)
    session.commit()

    # Print the id of the new State object
    print(new_state.id)

    # Close the session
    session.close()
