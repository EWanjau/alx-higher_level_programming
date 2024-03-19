#!/usr/bin/python3
"""0-select_states connects using an ORM and manipulates
the database
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}'\
        ORDER BY `id` ASC".format(argv[4]))
    [print(state) for state in c.fetchall()]
