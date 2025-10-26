import unittest

from quantumsimulator.gate import SQRT_2
from quantumsimulator.qubit import Qubit


class QubitTestCase(unittest.TestCase):

    def test_qubit_init(self):
        qubit = Qubit(0, 1)
        assert qubit.alpha == 0
        assert qubit.beta == 1

    def test_qubit_str(self):
        qubit = Qubit(SQRT_2 / 2, -SQRT_2 / 2)
        assert qubit.__str__() == "Qubit(alpha=np.float64(0.7071067811865476), beta=np.float64(-0.7071067811865476))"


if __name__ == '__main__':
    unittest.main()
