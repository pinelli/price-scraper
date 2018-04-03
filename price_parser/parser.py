import requests
from bs4 import BeautifulSoup


def parse_refs(sites_refs):
        items = []
        for site_ref in sites_refs:
            items = items + parse_site(site_ref)
        return items


def parse_site(site_ref):
    page = requests.get(site_ref[1])
    data = page.text
    soup = BeautifulSoup(data, "html.parser")
    if site_ref[0] == 'ebay':
        return parse_ebay(soup)
    if site_ref[0] == 'foxtrot':
        return parse_foxtrot(soup)
    else:
        return []


def parse_ebay(soup):
    items = []
    for item in soup.findAll("li", {"class": "sresult lvresult clearfix li shic"}):
        lvprice = item.find("li", {"class": "lvprice prc"}).find("span", {"class": "bold"})
        price = lvprice.get_text().strip()

        title = item.find("h3", {"class": "lvtitle"}).get_text().strip()

        items.append([title, 'ebay.com', price.strip()])

    return items


def parse_foxtrot(soup):
    items = []
    for item in soup.findAll("div", {"class": "product-item "}):
        title = item["data-title"]
        price = item["data-price"]
        items.append([title, 'foxtrot.com.ua', price.strip()])
    return items
