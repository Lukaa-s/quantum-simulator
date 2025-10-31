from abc import ABC
from math import sqrt, pi, isclose, floor

import numpy as np

from quantumsimulator.gates import H, X
from quantumsimulator.operator import Operator
from quantumsimulator.operators import cz_operator
from quantumsimulator.register import Register
from quantumsimulator.types import Complex, QubitIndex


class Algorithm(ABC):
    pass


class Grover(Algorithm):

    @staticmethod
    def _create_init_state(n_qubits: QubitIndex):
        full = np.full(1, 1, dtype=Complex)
        zeros = np.zeros(2 ** n_qubits - 1, dtype=Complex)
        values = np.concatenate([full, zeros])
        # value = 1 / n
        register = Register(n_qubits, values=values)
        register = H.apply_on_all_qubits(register)
        return register

    @staticmethod
    def run(n_qubits: QubitIndex, u: Operator):
        cz = cz_operator(n_qubits)
        register = Grover._create_init_state(n_qubits)
        nb_iter = floor(pi / 4 * sqrt(2 ** n_qubits))
        assert isclose(register.norm(), 1)
        for idx in range(nb_iter):
            # H X Z X H
            register = u @ register
            assert isclose(register.norm(), 1)
            register = H.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = X.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = cz @ register
            assert isclose(register.norm(), 1)
            register = X.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = H.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
        return register
