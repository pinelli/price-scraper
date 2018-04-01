from lxml import html
import requests
from bs4 import BeautifulSoup


def parse(sitesL):
    return [["IPhone X", "citrus.ua", 20_000],
            ["IPhone X_1", "citrus.ua", 20_000],
            ["GoPro HERO 6", "citrus.ua", 16_000],
            ["GoPro HERO 6", "foxtrot.ua", 14_000],
            ["IPhone X", "comfy.ua", 20_000],
            ["IPhone X", "aliexpress.com", 200]]


def parse_site():
        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        tree = html.fromstring(page.content)

        # This will create a list of buyers:
        buyers = tree.xpath('//div[@title="buyer-name"]/text()')
        # This will create a list of prices
        prices = tree.xpath('//span[@class="item-price"]/text()')

        print ('Buyers: ', buyers)
        print ('Prices: ', prices)


def parse_site_1():
        # soup = BeautifulSoup(page)  # page - скачиваем страницу и отдаем ее
        # for item in soup.findAll("div", {"class": "product"}):
        #     img = item.find("img")["src"]
        #     name = soup.find("tr", {"class": "name"})
        #     id = soup.find("tr", {"class": "id"})
        page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xiphone.TRS0&_nkw=iphone&_sacat=0")
        data = page.text
        soup = BeautifulSoup(data, "html.parser")
        items = parse_ebay(soup)
        return items


def parse_ebay(soup):
    items = []
    for item in soup.findAll("li", {"class": "sresult lvresult clearfix li shic"}):
        lvprice = item.find("li", {"class": "lvprice prc"})
        title = item.find("h3", {"class": "lvtitle"})

        bold_span = lvprice.find("span", {"class": "bold"})
        price = bold_span.get_text().strip()[:-1]
        items.append([title.get_text(), 'ebay.com', price.strip()])
        # print(title.get_text())
        # print(price.strip())

    return items

