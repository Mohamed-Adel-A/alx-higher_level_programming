#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ main function ""
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user,
                         passwd=db_passwd,
                         database = db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    data = cur.fetchall()

    for row in data:
        print(row)

    cur.close()
    db.close()
