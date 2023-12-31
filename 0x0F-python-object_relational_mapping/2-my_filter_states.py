#!/usr/bin/python3


""" Query"""

import MySQLdb
import sys


if __name__ == "__main__":
    ar = sys.argv
    username = ar[1]
    password = ar[2]
    database = ar[3]
    stateNameSearched = ar[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database, port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY'{}' \
                    ORDER BY id ASC ".format(stateNameSearched))
    states = cursor.fetchall()
    for state in states:
        print(state)
    # cursor.close()
    db_connection.close()
