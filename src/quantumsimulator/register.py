from typing import Self

import numpy as np
from numpy.linalg import matrix_power

I2 = np.identity(2)

QubitIndex = int


class Register:

    def __init__(self, n_qubits: int, values: np.ndarray[complex] = np.zeros(0)):
        self.n_qubits = n_qubits
        if values.size == 0:
            self.values = np.zeros(2 ** n_qubits, dtype=complex)
        else:
            if values.size != 2 ** n_qubits:
                raise Exception(f"size: {values.size} != {2 ** n_qubits}")
            self.values = values

    # FIXME init with what ?

    def set_value(self, idx: QubitIndex, value: complex):
        self.values[idx] = value

    def get_value(self, idx: QubitIndex) -> complex:
        return self.values[idx]


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


class Gate_n:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix = np.array(matrix_values)

    @staticmethod
    def init(matrix: np.ndarray[complex]) -> Self:
        gate_n = Gate_n([])
        gate_n.matrix = matrix
        return gate_n

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
        return Gate_n(self.matrix * other)

    def __rmul__(self, other) -> Self:
        return Gate_n(self.matrix * other)

    def __truediv__(self, other) -> Self:
        return Gate_n(self.matrix / other)

    def __matmul__(self, other) -> Self:
        return Gate_n(self.matrix @ other.matrix)

    def __pow__(self, power, modulo=None):
        return Gate_n.init(matrix_power(self.matrix, power))

    def __str__(self):
        return self.matrix.__str__()

    def __repr__(self):
        return self.matrix.__repr__()

    def __eq__(self, other):
        return self.matrix.__eq__(other.matrix).all()


SQRT_2 = np.sqrt(2)

H = Gate_n([[1, 1],
           [1, -1]]) / SQRT_2
I = Gate_n([[1, 0],
           [0, 1]])
X = Gate_n([[0, 1],
           [1, 0]])
NOT = X
Y = Gate_n([[0, -1j],
           [1j, 0]])
Z = Gate_n([[1, 0],
           [0, -1]])
S = Gate_n([[1, 0],
           [0, -1j]])
T = Gate_n([[1, 0],
           [0, SQRT_2 / 2]])


CNOT = Gate_n([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0],
               ])
