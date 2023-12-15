#!/usr/bin/python3


""" Query"""

import MySQLdb
import sys


if __name__ == "__main__":
    ar = sys.argv
    username = ar[1]
    password = ar[2]
    database = ar[3]

    db_connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database, port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%'\
                    ORDER BY id ASC ")
    states = cursor.fetchall()
    for state in states:
        print(state)

    db_connection.close()
