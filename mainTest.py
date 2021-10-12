import unittest
from .getProduct import getProduct

class MyTestCase(unittest.TestCase):
    def test_small_lists(self):
        test1 = [1, 10, 2, 6, 5, 3]
        test2 = [10, 6, 5, 2, 3, 1]
        test3 = [35, 86, 97, 65, 86, 53, 94, 15, 64, 74]
        test4 = [52, 65, 26, 58, 84, 33, 37, 38, 85, 82]
        test5 = [59, 29, 85, 29, 41, 85, 55, 59, 31, 57]


        self.assertEqual(getProduct(test1), 300)
        self.assertEqual(getProduct(test2), 300)
        self.assertEqual(getProduct(test3), )

    def test_random_list(self):
        random1 = [1, 1, -1]
        self.assertEqual(getProduct(random1), )


       




if __name__ == '__main__':
    unittest.main()
