import unittest
from .getProduct import getProduct

class MyTestCase(unittest.TestCase):
    def test_small_list(self):
        test1 = [1, 10, 2, 6, 5, 3]
        test2 = [1, 10, 2, 6, 5, 3, 1, 10, 2, 6, 5, 3]
        self.assertEqual(getProduct(test1), 300)
        self.assertEqual(getProduct(test2), 600)

    def test_random_list(self):
        random1 = [1, 1, -1]
        self.assertEqual(getProduct(random1), )


       




if __name__ == '__main__':
    unittest.main()
