from xml.dom import minidom
from xml.dom.minidom import Document


def read_sites(shops_file_path):
    """parses an xml file by name"""

    mydoc = minidom.parse(shops_file_path)
    references = mydoc.getElementsByTagName('ref')

    refs = []
    for elem in references:
        shop = elem.getAttribute('shop')
        refs.append([shop, elem.firstChild.data])
    return refs


def write_result(goods):
    doc = Document()
    root = doc.createElement('goods')
    doc.appendChild(root)

    for good_key in goods:
        name = doc.createElement('name')
        name_text = doc.createTextNode(good_key)
        name.appendChild(name_text)

        shops = doc.createElement('shops')

        for item in goods.get(good_key):
            shop_name_text = doc.createTextNode(item[0])
            shop_name = doc.createElement("name")
            shop_name.appendChild(shop_name_text)

            shop_price_text = doc.createTextNode(item[1])
            shop_price = doc.createElement("price")
            shop_price.appendChild(shop_price_text)

            shop = doc.createElement('shop')
            shop.appendChild(shop_name)
            shop.appendChild(shop_price)

            shops.appendChild(shop)

        good = doc.createElement('good')
        good.appendChild(name)
        good.appendChild(shops)

        root.appendChild(good)

        file = open('prices.xml', 'w')
        file.write(doc.toprettyxml(indent='\t'))


