#!/usr/bin/python3
"""0-select_states connects using an ORM and manipulates
mysql
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """connects to the database and selects records from a table"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
