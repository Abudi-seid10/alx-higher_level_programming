#!/usr/bin/python3
"""
 script that lists all State objects that contain the
 letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    for state in session.query(State).filter(State.name.like('%a%')):
        print(f'{state.id}: {state.name}')
    session.close()
