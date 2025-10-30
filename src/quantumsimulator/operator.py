import numpy as np

from quantumsimulator.register import Register


class Operator:
    def __init__(self, n_qubits: int, values: np.ndarray[complex]):
        self.n_qubits = n_qubits
        self.values = values

    def __matmul__(self, other: Register):
        if isinstance(other, Register):
            return Register(self.n_qubits, self.values @ other.values)
        raise NotImplemented


def cz(n_qubits: int) -> Operator:
    matrix = np.identity(2 ** n_qubits, dtype=complex)
    matrix[-1, -1] = -1
    return Operator(n_qubits, matrix)
