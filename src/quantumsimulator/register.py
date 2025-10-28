import numpy as np
from quantumsimulator.tensor import Tensor

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


class Gate1:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix = np.array(matrix_values)

    @staticmethod
    def tensor_power(matrix: np.ndarray, n: int) -> np.ndarray:
        if n == 0:
            return np.identity(1)
        if n == 1:
            return np.identity(np.size(matrix))
        return np.tensordot(matrix, Gate1.tensor_power(matrix, n - 1))

    def apply(self, register: Register, qubit_index: QubitIndex) -> Register:
        identity_before = Gate1.tensor_power(I2, qubit_index)
        identity_after = Gate1.tensor_power(I2, register.n_qubits - qubit_index - 1)
        before_dot_matrix = np.kron(identity_before, self.matrix)
        transform_matrix = np.kron(before_dot_matrix, identity_after)
        values = transform_matrix.dot(register.values)
        return Register(register.n_qubits, values)


SQRT_2 = np.sqrt(2)

H = Gate1([[1 / SQRT_2, 1 / SQRT_2],
           [1 / SQRT_2, -1 / SQRT_2]])


class Gate2:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix = np.array(matrix_values)

    def apply(self, register: Register, qubit_index1: QubitIndex, qubit_index2: QubitIndex) -> Register:
        pass


class Gate_n:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix = np.array(matrix_values)

    def apply(self, register: Register, qubit_indices: list[QubitIndex]) -> Register:
        u = self.matrix
        qubit_positions = [k for k in range(register.n_qubits)]
        swaps = {}
        for i in qubit_indices:
            if qubit_indices[i] != i:
                # swap qubit i and qubit_indices[i]
                swaps[i] = qubit_indices[qubit_positions[i]]
                temp = qubit_positions[i]
                qubit_positions[i] = qubit_positions[qubit_indices[i]]  # swap
                qubit_positions[qubit_indices[i]] = temp
                # update matrix

        return u * register


CNOT = Gate2([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0],
              ])
