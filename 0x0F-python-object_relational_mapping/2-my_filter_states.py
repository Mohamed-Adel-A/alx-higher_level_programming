#!/usr/bin/python3
"""
a script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_passwd,
                         database=db_name)
    cur = db.cursor()
    query = """SELECT * FROM states
             WHERE name = '{}'
             ORDER BY id ASC;""".format(sys.argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
