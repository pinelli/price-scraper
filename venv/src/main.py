import xml_r_w
import parser

SHOPS_PATH = "shops.xml"


def main():
    sites_l = xml_r_w.read_sites(SHOPS_PATH)
    print("Shops:\n", sites_l)

    items_l = parser.parse(sites_l)
    print("Items:\n", items_l)

    print("Goods: ", arrange_goods(items_l))


def arrange_goods(items_l):
    if not items_l:
        return None
    else:
        goods = {items_l[0][0]: [[items_l[0][1], items_l[0][2]]]}
        for i in range(1, len(items_l)):
            good = items_l[i][0]
            shop_price_entry = goods.get(good)
            if shop_price_entry is None:
                goods[good] = [[items_l[i][1], items_l[i][2]]]
            else:
                shop_price_entry.append([items_l[i][1], items_l[i][2]])

    return goods


main()
