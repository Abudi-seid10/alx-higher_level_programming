#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (argv[4],))
    row = cur.fetchall()
    for i in row:
        print(i)

    cur.close()
    conn.close()
