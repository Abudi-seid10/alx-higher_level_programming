#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    curr = conn.cursor()
    curr.execute("SELECT cities.id, cities.name, states.name FROM cities,"
                 " states WHERE cities.state_id=states.id")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    conn.close()
