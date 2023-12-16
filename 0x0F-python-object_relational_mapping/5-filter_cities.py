#!/usr/bin/python3
""" Query"""


import MySQLdb
import sys


if __name__ == "__main__":
    ar = sys.argv
    username = ar[1]
    password = ar[2]
    database = ar[3]
    stateName = ar[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database, port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states as s ON cities.state_id = s.id \
                    WHERE s.name = %s \
                    ORDER BY cities.id ASC", (stateName,))
    cities = cursor.fetchall()
    # result = ''.join(tup)
    for city in cities:
        print("{}".format(city), end='')

        # print("{}".format(city))
        # print(f{{ch}}, city)

    db_connection.close()
