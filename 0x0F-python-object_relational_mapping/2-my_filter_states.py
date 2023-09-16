#!/usr/bin/python3
"""
    Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
        Take 3 arguments username, password, db_name
    """
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(
        user=username,
        host="localhost",
        port=3306,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name\
            LIKE BINARY '{}' ORDER BY id ASC".format(state_name))

    for row in cursor.fetchall():
        print(row)

