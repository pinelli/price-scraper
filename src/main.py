import xml_r_w
import parser
import Levenshtein_search

SHOPS_PATH = "shops.xml"
LEV_DIST = 2


def main():

    sites_l = xml_r_w.read_sites(SHOPS_PATH)
    print("Shops:\n", sites_l)

    items_l = parser.parse_site_1() #parser.parse(sites_l)
    print("Items:\n", items_l)

    print("Goods: ", arrange_goods(items_l))

    print("-------------")
    # items = parser.parse_site_1()
    # print("ITEMS: ", items)


class GoodWrapper:
    def __init__(self, string):
        self.string = string

    def leven_dist(self, string):
        return string == self.string

    def __eq__(self, other):
        return self.leven_dist(other)

    def __hash__(self):
        return hash(self.string)

    def __str__(self):
        return self.string


def leven_dist(str1, str2):

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
            #shop_price_entry = goods.get(good)
            shop_price_entry = similar_good(good, goods)
            if shop_price_entry is None:
                goods[good] = [[items_l[i][1], items_l[i][2]]]
            else:
                shop_price_entry.append([items_l[i][1], items_l[i][2]])

    return goods


main()

# wordset = Levenshtein_search.populate_wordset(-1, ["lo5l7"])
# result = Levenshtein_search.lookup(wordset, "lol", LEV_DIST)
# print(not not result)