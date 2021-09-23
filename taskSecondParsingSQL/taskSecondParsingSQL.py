# Task second parsing sql
# Parsing text in SQL (From tex to select keywords, text and keywords at the discretion of the candidate)

# This file is parsed by the site stopgame.ru using python and add data to the database via sql queries.
# I didn't understand the task exactly how to do parsing, so I did it this way.
# Link to stopgame.ru: https://stopgame.ru/review/new/izumitelno

# import packages
import requests
from bs4 import BeautifulSoup as BS

# import package sqlite3 to work with database
import sqlite3

# number of pages
page = 1

# sum of elements
sum = 0

# connect to database
conn = sqlite3.connect("games.db")

cursor = conn.cursor()

# parsing loop and add data of games to database
while True:
    r = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select(".items > .article-summary")

    if len(items):
        for el in items:
            title = el.select(".caption > a")
            print(title[0].text)
            print(sum)
            sum += 1
            # sql queries
            cursor.executemany("INSERT INTO games VALUES (?)", title[0].text)
        page += 1
    else:
        break

conn.commit()
conn.close()