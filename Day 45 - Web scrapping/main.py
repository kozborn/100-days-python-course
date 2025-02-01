from bs4 import BeautifulSoup
import requests
#
# with open('./website.html') as file:
#     website = file.read()
#
# # soup = BeautifulSoup(website, 'lxml')
# soup = BeautifulSoup(website, 'lxml')
#
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a.get_text())
# print(soup.a.get('href'))
# print(soup.find_all('li'))
#
# print(soup.select(selector=".heading"))
# print(soup.select_one(selector=".heading"))
#
# print(soup.select_one(selector="#name"))
#
# print(soup.find_all("li", "a"))


url = "https://news.ycombinator.com/"

website = requests.get(url)
website.raise_for_status()
soup = BeautifulSoup(website.text, 'lxml')

title_rows = soup.select("td.title span.titleline > a")

scores = soup.select(".subtext > span")
print(len(title_rows), len(scores))

for title in title_rows:
    print(title.text)

for score in scores:
    print(score.text)

# titles = soup.select(selector=".title")
#
# print(titles)


