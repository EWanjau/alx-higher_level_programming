#!/usr/bin/python3
"""this module lists all records from a table fitting a certain criteria
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    """connects to the database and selects records from a table which start with 'N'"""
    db=MySQLdb.connect(user=argv[1],passwd=argv[2],db=argv[3])
    c=db.cursor()
    c.execute("SELECT * FROM states WHERE upper(left(name,1))='N' ORDER BY `state.id` ASC")
    [print(state) for state in c.fetchall()]
