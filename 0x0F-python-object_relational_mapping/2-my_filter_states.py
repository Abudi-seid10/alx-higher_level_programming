#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' "
                "ORDER BY id".format(argv[4]))
    row = cur.fetchall()
    for i in row:
        if i[1] == argv[4]:
            print(i)

    cur.close()
    conn.close()
