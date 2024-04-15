#!/usr/bin/python3
"""Script to delete all State objects with a name containing the letter 'a' from the database"""

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

    # Query all State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each State object containing the letter 'a'
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
