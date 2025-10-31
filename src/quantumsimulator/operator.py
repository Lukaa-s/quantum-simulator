from numpy import isclose

from quantumsimulator.register import Register
from quantumsimulator.types import CArray, QubitIndex


class Operator:
    def __init__(self, n_qubits: QubitIndex, values: CArray):
        self.n_qubits = n_qubits
        self.values = values

    def __matmul__(self, other: Register):
        if isinstance(other, Register):
            return Register(self.n_qubits, self.values @ other.values)
        raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, Operator):
            return self.n_qubits == other.n_qubits and isclose(self.values, other.values).all()
        raise NotImplemented
