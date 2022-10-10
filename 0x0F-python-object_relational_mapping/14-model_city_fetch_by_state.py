#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    city_state = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id).all()
    for cities, state in city_state:
        print('{}: ({}) {}'.format(state.name, cities.id, cities.name))
    session.close()
