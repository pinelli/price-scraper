import unittest
from price_parser import main


class TestPriceParser(unittest.TestCase):

    def test_levenshtein(self):
        dist = main.leven_dist('string1', "string")
        self.assertEqual(dist, 1)

    def test_similar_good(self):
        res = main.similar_good('g', {'g': [['comp1', 'price1'], ['comp2', 'price2']]})
        self.assertEqual(res, [['comp1', 'price1'], ['comp2', 'price2']])

        res = main.similar_good("some_good", {'g': [['comp1', 'price1'], ['comp2', 'price2']]})
        self.assertEqual(res, None)

        res = main.similar_good("s", {'g': [['comp1', 'price1'], ['comp2', 'price2']]})
        self.assertEqual(res, [['comp1', 'price1'], ['comp2', 'price2']])

        res = main.similar_good("abcd", {'12345': [['comp1', 'price1'], ['comp2', 'price2']],
                                'abcde': [['comp3', 'price3'], ['comp4', 'price4'], ['comp5', 'price5']],
                                 '678910': [['comp6', 'price6'], ['comp7', 'price7']]})
        self.assertEqual(res, [['comp3', 'price3'], ['comp4', 'price4'], ['comp5', 'price5']])

    def test_arrange_goods(self):
        res = main.arrange_goods([['good1', 'site1', 'price1']])
        self.assertEqual(res, {'good1': [['site1', 'price1']]})

        res = main.arrange_goods([['good1', 'site1', 'price1'], ['good1', 'site2', 'price2']])
        self.assertEqual(res, {'good1': [['site1', 'price1'], ['site2', 'price2']]})

        res = main.arrange_goods([['goodAAAA', 'site1', 'price1'], ['goodA', 'site2', 'price2']])
        self.assertEqual(res, {'goodAAAA': [['site1', 'price1']], 'goodA': [['site2', 'price2']]})
