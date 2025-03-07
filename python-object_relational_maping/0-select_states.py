#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: MySQL username, password, and database name.
Results are sorted in ascending order by states.id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cursor = db.cursor()
    
    # Execute SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch and print results
    for row in cursor.fetchall():
        print(row)
    
    # Clean up
    cursor.close()
    db.close()

