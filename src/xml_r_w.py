from xml.dom import minidom


def read_sites(shops_file_path):
    # parse an xml file by name
    mydoc = minidom.parse(shops_file_path)
    shopElements = mydoc.getElementsByTagName('shop')

    shops = []
    for elem in shopElements:
        shops.append(elem.firstChild.data)
    return shops
