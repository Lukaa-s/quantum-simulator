import numpy as np

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

    def set_value(self, idx: QubitIndex, value: complex):
        self.values[idx] = value

    def get_value(self, idx: QubitIndex) -> complex:
        return self.values[idx]

    def __str__(self):
        return self.values.__str__()

    def __repr__(self):
        return self.values.__repr__()

    def __eq__(self, other):
        return np.allclose(self.values, other.values)
