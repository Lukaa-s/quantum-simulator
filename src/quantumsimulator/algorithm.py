from abc import ABC
from math import sqrt, pi, ceil, isclose, floor

import numpy as np

from quantumsimulator.gates import H, X, Z
from quantumsimulator.register import Register


class Algorithm(ABC):
    pass


class Grover(Algorithm):

    @staticmethod
    def _create_init_state(n_qubits):
        values = np.concatenate([np.full(1, 1, dtype=complex),
                                 np.zeros(2 ** n_qubits - 1, dtype=complex)])
        # value = 1 / n
        register = Register(n_qubits, values=values)
        register = H.apply_on_all_qubits(register)
        return register

    def run(self, n_qubits: int, U: np.ndarray[complex]):
        CZ = np.identity(2 ** n_qubits, dtype=complex)
        CZ[-1, -1] = -1
        register = Grover._create_init_state(n_qubits)
        nb_iter = floor(pi / 4 * sqrt(2 ** n_qubits))
        assert isclose(register.norm(), 1)
        for iter in range(nb_iter):
            # H X Z X H
            register = Register(register.n_qubits, U @ register.values)
            # register = U.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = H.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = X.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = Register(register.n_qubits,CZ @ register.values)
            #assert isclose(register.norm(), 1)
            register = X.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
            register = H.apply_on_all_qubits(register)
            assert isclose(register.norm(), 1)
        return register
