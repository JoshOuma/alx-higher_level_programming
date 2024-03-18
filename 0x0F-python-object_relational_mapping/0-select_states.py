#!/usr/bin/python3
"""
This module connects to a MySQL database and fetches data from the 'states' table.
"""

import MySQLdb
import sys

def fetch_data_from_db(username, password, db_name):
    """
    This function connects to a MySQL database using the provided username, password, and database name.
    It fetches data from the 'states' table and prints each row.
    """
    db = MySQLdb.connect(host="localhost", username=username, password=password, db=db_name, port=3306)
    curr = db.cursor()
    curr.execute("select * from states ORDER BY id ASC")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()

if __name__ == '__main__':
    """
    Main function that calls 'fetch_data_from_db' with command line arguments.
    """
    fetch_data_from_db(sys.argv[1], sys.argv[2], sys.argv[3])
