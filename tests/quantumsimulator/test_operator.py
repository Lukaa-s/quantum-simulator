import numpy as np

from quantumsimulator.operator import Operator
from quantumsimulator.register import Register
from quantumsimulator.types import Complex


class TestOperator:

    def test_init(self):
        operator = Operator(3, np.identity(2 ** 3, dtype=Complex))
        assert operator.n_qubits == 3

    def test_operations(self):
        operator = Operator(3, np.identity(2 ** 3, dtype=Complex) * 2)
        register = Register(3, np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=complex))
        expected = Register(3, np.array([2, 4, 6, 8, 10, 12, 14, 16], dtype=complex))
        result = operator @ register
        assert result == expected
