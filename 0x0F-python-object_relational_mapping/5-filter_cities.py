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
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=username,
        host="localhost",
        port=3306,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()
    query = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)
