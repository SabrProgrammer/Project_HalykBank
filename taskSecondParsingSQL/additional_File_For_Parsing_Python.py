# Additional file for parsing python
# I added an additional file for parsing using python without using sql.
# I did not understand the task and made two files for parsing and
# this file to parse the site stopgame.ru and display the number of games with the rating "amazing".
# Link to stopgame.ru: https://stopgame.ru/review/new/izumitelno

# import packages
import requests
from bs4 import BeautifulSoup as BS

# number of page
page = 1

# sum of elements
sum = 0

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
        page += 1
    else:
        break
