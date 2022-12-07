#!/usr/bin/python3
"""0-selects cities connects using an ORM and manipulates
the database
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT c.name\
        FROM cities as c \
            INNER JOIN states as s \
            ON c.state_id = s.id \
            WHERE BINARY s.name = '{}'\
        ORDER BY c.id ASC".format(argv[4]))
    print(", ".join(city[0] for city in c.fetchall()))
