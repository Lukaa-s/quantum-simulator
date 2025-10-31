import numpy as np

from quantumsimulator.operator import Operator
from quantumsimulator.operators import cz_operator


class TestOperator:

    def test_init(self):
        cz = cz_operator(2)
        expected = Operator(2, np.array([[1, 0, 0, 0],
                                         [0, 1, 0, 0],
                                         [0, 0, 1, 0],
                                         [0, 0, 0, -1]], dtype=complex))
        assert cz == expected
