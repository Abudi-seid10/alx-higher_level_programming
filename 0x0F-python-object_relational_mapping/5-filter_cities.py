#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    curr = conn.cursor()
    curr.execute("SELECT cities.name FROM cities JOIN states ON"
                 " cities.state_id=states.id WHERE states.name LIKE %s"
                 " ORDER BY cities.id", ({argv[4]}))
    rows = curr.fetchall()
    print(", ".join(row[0] for row in rows))
    curr.close()
    conn.close()
