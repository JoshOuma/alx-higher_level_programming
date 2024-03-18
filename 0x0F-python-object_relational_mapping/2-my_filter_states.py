#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db= MySQLdb.connect(host="localhost",user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3],name=sys.argv[4],port=3306)
    curr=db.cursor()
    curr.execute("select * from states where name LIKE BINARY '{}' ORDER BY ASC".format(sys.argv[4]))
    rows=curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()