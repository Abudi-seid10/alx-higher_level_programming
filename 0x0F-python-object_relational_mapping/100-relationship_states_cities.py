#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from relationship_city import Base, City, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    new_state = State(name='Cali')
    session.add(new_state)
    session.commit()
    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()
