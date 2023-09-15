#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("""SELECT c.id, c.name, s.name
                   FROM cities c
                   INNER JOIN states s 
                   ON c.state_id=s.id
                   WHERE s.name = %s
                   ORDER BY c.id ASC""",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
