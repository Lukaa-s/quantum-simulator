from typing import Self

import numpy as np
from numpy.linalg import matrix_power

from quantumsimulator.register import Register, QubitIndex


def binary_conversion(n: int, length: int) -> list[int]:
    """Convert n to binary representation with given length."""

    bin_repr = [0] * length
    for i in range(length - 1, -1, -1):
        bin_repr[i] = n % 2
        n = n // 2
    return bin_repr


def inverse_binary_conversion(bin_repr: list[int]) -> int:
    """Convert binary representation back to integer."""
    n = 0
    length = len(bin_repr)
    for i in range(length):
        n += bin_repr[length - 1 - i] * (2 ** i)
    return n


class Gate:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix = np.array(matrix_values)

    @staticmethod
    def init(matrix: np.ndarray[complex]) -> Self:
        gate = Gate([])
        gate.matrix = matrix
        return gate

    def apply(self, register: Register, qubit_indices: list[QubitIndex]) -> Register:
        u = self.matrix

        qubit_positions = [k for k in range(register.n_qubits) if k not in qubit_indices] + qubit_indices
        P = np.zeros((2 ** register.n_qubits, 2 ** register.n_qubits), dtype=complex)
        for i in range(2 ** register.n_qubits):
            # convert in binary
            bin_repr = binary_conversion(i, register.n_qubits)
            permuted_bin_repr = [bin_repr[k] for k in qubit_positions]
            j = inverse_binary_conversion(permuted_bin_repr)
            P[j, i] = 1

        u_tild = np.kron(np.identity(2 ** (register.n_qubits - len(qubit_indices)), dtype=complex), u)
        u_total = P.T @ u_tild @ P
        return Register(register.n_qubits, u_total @ register.values)

    def __mul__(self, other) -> Self:
        return Gate(self.matrix * other)

    def __rmul__(self, other) -> Self:
        return Gate(self.matrix * other)

    def __truediv__(self, other) -> Self:
        return Gate(self.matrix / other)

    def __matmul__(self, other) -> Self:
        return Gate(self.matrix @ other.matrix)

    def __pow__(self, power, modulo=None):
        return Gate.init(matrix_power(self.matrix, power))

    def __str__(self):
        return self.matrix.__str__()

    def __repr__(self):
        return self.matrix.__repr__()

    def __eq__(self, other):
        return self.matrix.__eq__(other.matrix).all()
