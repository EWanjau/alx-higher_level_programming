"""0-select_states connects using an ORM and manipulates
mysql
"""

if __name__ == "__main__":
    """connects to the database and selects records from a table"""
    import sys
    import MySQLdb
    db = MySQLdb.connect(host=sys.argv[1], user=sys.argv[2], passwd=sys.argv[3], db=sys.argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
