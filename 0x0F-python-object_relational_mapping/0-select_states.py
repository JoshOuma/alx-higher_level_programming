#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db=MySQLdb.connect(host="localhost",username= sys.argv[1],password=sys.argv[2],db=sys.argv[3],port=3306)
    curr=db.cursor()

    curr.execute("select * from states ORDER BY id ASC")
    rows=curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()