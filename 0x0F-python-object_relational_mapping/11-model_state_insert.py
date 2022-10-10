#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa
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
    new_state = State(name='Louisiana')
    session = session()
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana').first()
    print(state.id)
    session.close()
