import unittest
from sample.getProduct import getProduct

class MyTestCase(unittest.TestCase):

    def test_len3_list(self):
        lst1 = [5, 1, 10]
        lst2 = [2, 6, 10]
        lst3 = [10,3, 34]
        lst4 = [1, 43, 40]

        self.assertEqual(getProduct(lst1), 50)
        self.assertEqual(getProduct(lst2), 120)
        self.assertEqual(getProduct(lst3), 1020)
        self.assertEqual(getProduct(lst4), 1720)

    def test_small_lists(self):
        test1 = [1, 10, 2, 6, 5, 3]
        test2 = [10, 6, 5, 2, 3, 1]
        test3 = [35, 86, 97, 65, 86, 53, 94, 15, 64, 74]
        test4 = [52, 65, 26, 58, 84, 33, 37, 38, 85, 82]
        test5 = [59, 29, 85, 29, 41, 85, 55, 59, 31, 57]


        self.assertEqual(getProduct(test1), 300)
        self.assertEqual(getProduct(test2), 300)
        self.assertEqual(getProduct(test3), 784148)
        self.assertEqual(getProduct(test4), 585480)
        self.assertEqual(getProduct(test5), 426275)

    def test_negative_numbers(self):
        nTest1 = [-1, 2, -5]
        nTest2 = [-35, -86, -97, -65, -86, -53, -94, -15, -64, -74]
        nTest3 = [-10, -6, -5, -2, -3, -1]
        nTest4 = [-1, -10, -2, -6, -5, -3]
        nTest5 = [-4, -5, -1, -9, -55]

        self.assertEqual(getProduct(nTest1), 10)
        self.assertEqual(getProduct(nTest2), -27825)
        self.assertEqual(getProduct(nTest3), -6)
        self.assertEqual(getProduct(nTest4), -6)
        self.assertEqual(getProduct(nTest5), -20)

if __name__ == '__main__':
    unittest.main()
