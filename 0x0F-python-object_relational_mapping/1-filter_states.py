#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """ main function """
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_passwd,
                         database=db_name)
    cur = db.cursor()
    query = """SELECT * FROM states
               WHERE name LIKE BINARY 'N%'
               ORDER BY id ASC;"""
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
