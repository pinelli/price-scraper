from xml.dom import minidom
from xml.dom.minidom import Document

def read_sites(shops_file_path):
    """parse an xml file by name"""

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

        good = doc.createElement('good')
        good.appendChild(name)
        good.appendChild(shop)

        root.appendChild(good)

        file = open('prices.xml', 'w')
        file.write(doc.toprettyxml(indent='\t'))

    # for i in range(1, 3):
    #     main = doc.createElement('item')
    #     main.attributes['class'] = 'memory'
    #     root.appendChild(main)
    #     for j in range(1, 3):
    #         p = doc.createElement('p')
    #         text = doc.createTextNode('DIMM Size' + str(j))
    #         p.appendChild(text)
    #         main.appendChild(p)


