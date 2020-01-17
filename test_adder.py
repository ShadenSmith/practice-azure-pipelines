
import unittest

import torch
import adder
import pathlib

class TestAdder(unittest.TestCase):
    def test_add(self):
        result = adder.add(2,3)
        self.assertTrue(result == 5)

    def test_add2(self):
        result = adder.add(3, -3)
        self.assertTrue(result == 0)

    def test_add3(self):
        result = adder.add3(1, 2, 3)
        self.assertTrue(result == 6)

    def test_gpu(self):
        pass
        #self.assertTrue(torch.cuda.is_available())

    def test_artifact(self):
        pathlib.Path('logs').mkdir(parents=True, exist_ok=True)
        with open('logs/test_output.log', 'w') as fout:
            print('Test output', file=fout)


if __name__ == '__main__':
    unittest.main()


