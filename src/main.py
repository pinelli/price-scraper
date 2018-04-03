import xml_r_w
import parser
import Levenshtein_search

SHOPS_PATH = "references.xml"
LEV_DIST = 2


def main():
    sites_refs = xml_r_w.read_sites(SHOPS_PATH)
    print("Shops:\n", sites_refs)

    items = parser.parse_refs(sites_refs)
    print("Items:\n", items)

    goods = arrange_goods(items)
    print("Goods: ", goods)

    xml_r_w.write_result(goods)


def leven_dist(str1, str2):
    return False
    wordset = Levenshtein_search.populate_wordset(-1, [str1])
    result = Levenshtein_search.lookup(wordset, str2, LEV_DIST)
    return not not result


def similar_good(good, goods):
    for key, value in goods.items():
        if leven_dist(good, key):
            return value
    return None


def arrange_goods(items_l):
    if not items_l:
        return None
    else:
        goods = {items_l[0][0]: [[items_l[0][1], items_l[0][2]]]}
        for i in range(1, len(items_l)):
            good = items_l[i][0]
            shop_price_entry = similar_good(good, goods)
            if shop_price_entry is None:
                goods[good] = [[items_l[i][1], items_l[i][2]]]
            else:
                shop_price_entry.append([items_l[i][1], items_l[i][2]])

    return goods


main()
