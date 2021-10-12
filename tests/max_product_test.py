import unittest
from sample.max_product import max_product

class max_product_tests(unittest.TestCase):

    def test_len3_list(self):
        test1 = [5, 1, 10]
        test2 = [2, 6, 10]
        test3 = [10, 3, 34]
        test4 = [1, 43, 40]

        self.assertEqual(max_product(test1), 50)
        self.assertEqual(max_product(test2), 120)
        self.assertEqual(max_product(test3), 1020)
        self.assertEqual(max_product(test4), 1720)

    def test_small_lists(self):
        test1 = [1, 10, 2, 6, 5, 3]
        test2 = [10, 6, 5, 2, 3, 1]
        test3 = [35, 86, 97, 65, 86, 53, 94, 15, 64, 74]
        test4 = [52, 65, 26, 58, 84, 33, 37, 38, 85, 82]
        test5 = [59, 29, 85, 29, 41, 85, 55, 59, 31, 57]


        self.assertEqual(max_product(test1), 300)
        self.assertEqual(max_product(test2), 300)
        self.assertEqual(max_product(test3), 784148)
        self.assertEqual(max_product(test4), 585480)
        self.assertEqual(max_product(test5), 426275)

    def test_negative_numbers(self):
        test1 = [-1, 2, -5]
        test2 = [-35, -86, -97, -65, -86, -53, -94, -15, -64, -74]
        test3 = [-10, -6, -5, -2, -3, -1]
        test4 = [-1, -10, -2, -6, -5, -3]
        test5 = [-4, -5, -1, -9, -55]


        self.assertEqual(max_product(test1), 10)
        self.assertEqual(max_product(test2), -784148)
        self.assertEqual(max_product(test3), -10 * -6 * -5)
        self.assertEqual(max_product(test4), -300)
        self.assertEqual(max_product(test5), -2475)

if __name__ == '__main__':
    unittest.main()
