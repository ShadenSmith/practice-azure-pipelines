
import unittest

import adder

class TestAdder(unittest.TestCase):
    def test_add(self):
        result = adder.add(2,3)
        self.assertTrue(result == 5)

if __name__ == '__main__':
    unittest.main()


