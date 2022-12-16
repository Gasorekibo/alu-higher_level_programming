#!/usr/bin/python3
"""
    listing all states in a database
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
