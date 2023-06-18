#!/usr/bin/python3
"""0-select_states connects using an ORM and manipulates
the database mitigating risk from SQL injections
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == argv[4]]
