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


# url = "https://www.amazon.pl/Dyson-bezprzewodowy-elektroszczotka-litowo-jonowy-przechowywania/dp/B07NVYN6JQ"
#
# HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#                            'Accept-Language': 'en-US, en;q=0.5'})
#
# website = requests.get(url, headers=HEADERS)
# website.raise_for_status()
# soup = BeautifulSoup(website.text, 'lxml')
#
# price = soup.select_one('#corePrice_feature_div .a-price .a-offscreen')

# print(price.get_text())
price = "1 984,39zł"
new_string = ''.join(ch for ch in price if ch.isdigit() or ch == ',' or ch == '.')
print(price)
print(float(new_string.replace(',', '.')))
print(float(price.replace("zł", "").strip().replace("\xa0", "").replace(",", ".")))



