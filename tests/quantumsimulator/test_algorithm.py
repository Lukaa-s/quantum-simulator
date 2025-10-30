from math import sqrt

import numpy as np

from quantumsimulator.algorithm import Grover
from quantumsimulator.operator import Operator
from quantumsimulator.register import Register


class TestAlgorithm:

    def test_grover_init(self):
        n_qubits = 3
        init_state = Grover._create_init_state(n_qubits)
        value = 1 / sqrt(2 ** n_qubits)
        assert init_state == Register(n_qubits, np.full(2 ** n_qubits, value, dtype=complex))

    def test_grover(self):
        grover = Grover()
        U = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1],
        ]
        register = grover.run(2, Operator(2, np.array(U)))
        assert np.isclose(register.values, np.array([0, 0, -1, 0])).all()
