import requests
from bs4 import BeautifulSoup
import pandas as pd

pages = []
prices = []
stars = []
titles = []
stock = []
pages_to_scrape = 1

new_url = 'http://books.toscrape.com/'


#new_url = 'http://books.toscrape.com/' +soup.find("li", class_="next").find('a').get('href')
while new_url != '':
    source = requests.get(new_url).text
    soup = BeautifulSoup(source, "lxml")
    print(new_url)
    for each in soup.find("ol", class_="row").findAll('li'):
        prices.append(
            each.find('p', class_='price_color').text.split('£')[1].strip())
        stock.append(
            each.find('p', class_='instock availability').text.strip())
        titles.append(each.find('h3').text.strip())
        stars.append(each.find('p').get('class')[1])
    print(new_url)
    try:
        sopa = BeautifulSoup(source, "lxml").find(
            "li", class_="next").find('a').get('href')
        if new_url == 'http://books.toscrape.com/':
            new_url = 'http://books.toscrape.com/' + sopa
        else:
            new_url = 'http://books.toscrape.com/catalogue/' + sopa
    except:
        new_url = ''


data = {'titles': titles, 'prices': prices, 'stars': stars, 'stock': stock}

data = pd.DataFrame(data)
print(data[data.stars == 'Five'].sort_values('prices'))
