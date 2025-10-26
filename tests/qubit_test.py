import unittest

from quantumsimulator.gate import H
from quantumsimulator.qubit import Qubit

class MyTestCase(unittest.TestCase):
    def test_something(self):
        qubit = Qubit(0, 1)
        result = H.apply(qubit)
        print(result)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
