#!/usr/bin/python3
"""
    sort all starts with N from database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
