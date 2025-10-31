import numpy as np

from quantumsimulator.operator import Operator
from quantumsimulator.types import Complex, QubitIndex


def cz_operator(n_qubits: QubitIndex) -> Operator:
    matrix = np.identity(2 ** n_qubits, dtype=Complex)
    matrix[-1, -1] = -1
    return Operator(n_qubits, matrix)
