import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='security'
)

cur = con.cursor()

sql = f"""
    create database imransoft
"""

cur.execute(sql)
print("All done")
