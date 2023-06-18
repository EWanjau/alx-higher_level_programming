#!/usr/bin/python3
"""this module connects using an ORM and manipulates
mysql
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """connects to the database and selects records from a table"""
    db=MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    c=db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `state.id` ASC")
    [print(state) for state in c.fetchall()]
