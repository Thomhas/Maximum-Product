import unittest
from .getProduct import getProduct

class MyTestCase(unittest.TestCase):
    def test_product_max_three(self):
        self.assertEqual(True, True)
        test1 = [1, 10, 2, 6, 5, 3]
        test2 = [1, 10, 2, 6, 5, 3, 1, 10, 2, 6, 5, 3]
        self.assertEqual(getProduct(test1), 300)
        self.assertEqual(getProduct(test2), 600)
       




if __name__ == '__main__':
    unittest.main()
