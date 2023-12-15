#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    ar= sys.argv
    username = ar[1]
    password = ar[2]
    database = ar[3]
    try:
        db_connection= MySQLdb.connect(
            host= "localhost",
            user=username,
            passwd=password,
            db=database, port=3306)
        cursor=db_connection.cursor()
        cursor.execute("SELECT cities.id, cities.name, s.name AS state_name\
                       FROM cities \
                       JOIN states as s ON cities.state_id = s.id \
                       ORDER BY cities.id ASC")
        cities = cursor.fetchall()
        for city in cities:
            print(city)

        db_connection.close()
    except:
        print('connecting went wrong')

