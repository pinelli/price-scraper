import xml_r_w
import parser
import Levenshtein_search

SHOPS_PATH = "references.xml"
LEV_DIST = 2


def main():

    sites_refs = xml_r_w.read_sites(SHOPS_PATH)
    #print("Shops:\n", sites_refs)

    print('Parsing websites from "', SHOPS_PATH, '"')
    items = parser.parse_refs(sites_refs)
    #print("Items:\n", items)

    print('Processing goods list')
    goods = arrange_goods(items)
    print("Goods: ", goods)

    xml_r_w.write_result(goods)

    print('Done. Results are written in "prices.xml"')


def custom_lev_dist(a, b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n+1)  # Keep current and previous row, not entire matrix
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def leven_dist(str1, str2):
    distance = custom_lev_dist(str1, str2)
    return distance < LEV_DIST
    # wordset = Levenshtein_search.populate_wordset(-1, [str1])
    # result = Levenshtein_search.lookup(wordset, str2, LEV_DIST)
    # return not not result


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
