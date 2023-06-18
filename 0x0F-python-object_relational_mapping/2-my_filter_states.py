#!/usr/bin/python3
"""this module connects using an ORM and manipulates
mysql using msqldb module
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    """connects to the database and selects records from a
    table which match an argument"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name='arv[4]'\
        ORDER BY `state.id` ASC")
    [print(state) for state in c.fetchall()]
