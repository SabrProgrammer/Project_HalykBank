# create database games

import sqlite3

# connect to database
conn= sqlite3.connect("games.db")

# sql queries to creat table and select data
sql = "CREATE TABLE games (name TEXT)"
sql = "SELECT * FROM games"
cursor = conn.cursor()

cursor.execute(sql)

res = cursor.fetchall()

for r in res:
    print(r)

conn.close()