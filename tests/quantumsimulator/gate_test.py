import unittest

from quantumsimulator.gate import SQRT_2, H
from quantumsimulator.qubit import Qubit


class GateTestCase(unittest.TestCase):

    def test_gate_H(self):
        qubit = Qubit(0, 1)
        result = H.apply(qubit)
        assert result == Qubit(1 / SQRT_2, -1 / SQRT_2), "aaa"


if __name__ == '__main__':
    unittest.main()
