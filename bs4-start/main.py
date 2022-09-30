from bs4 import BeautifulSoup
# import lxml

with open("website.html",encoding="utf8") as file:
    contents1 = file.read()

soup = BeautifulSoup(contents1, "html.parser")
# print(soup.title.name)
# print(soup.li)