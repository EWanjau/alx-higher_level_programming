#!/usr/bin/python3
"""0-select_states connects using an ORM and manipulates
the database mitigating risk from SQL injections
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT c.id, c.name , s.name \
        FROM cities as c \
            INNER JOIN states as s \
            ON c.state_id = s.id \
            WHERE ORDER BY c.id ASC")
    [print(city) for city in c.fetchall()]
