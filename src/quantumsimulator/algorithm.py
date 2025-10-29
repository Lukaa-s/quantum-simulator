from abc import ABC

import numpy as np

from quantumsimulator.gates import H
from quantumsimulator.register import Register


class Algorithm(ABC):
    pass


class Grover(Algorithm):
    # H X Z X H

    @staticmethod
    def _create_init_state(n_qubits):
        values = np.concatenate([np.full(1, 1, dtype=complex),
                                 np.zeros(2 ** n_qubits - 1, dtype=complex)])
        # value = 1 / n
        register = Register(n_qubits, values=values)
        for q_idx in range(0, n_qubits):
            register = H.apply(register, [q_idx])
        return register

    def run(self, n_qubits: int):
        init_register = Grover._create_init_state(n_qubits)
