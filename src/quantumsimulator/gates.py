import numpy as np

from quantumsimulator.gate import Gate
from quantumsimulator.types import Complex

SQRT_2 = np.sqrt(2)

H = Gate.build([[1, 1],
                [1, -1]]) / SQRT_2
I = Gate.build([[1, 0],
                [0, 1]])
X = Gate.build([[0, 1],
                [1, 0]])
NOT = X
Y = Gate.build([[0, -1j],
                [1j, 0]])
Z = Gate.build([[1, 0],
                [0, -1]])
S = Gate.build([[1, 0],
                [0, -1j]])
T = Gate.build([[1, 0],
                [0, SQRT_2 / 2]])

CNOT = Gate.build([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 1, 0],
                   ])


def _toffoli_3x3():
    """Matrice 8x8 de la Toffoli (CCNOT) avec contrôles sur les deux bits
    les plus significatifs et cible = bit le moins significatif de ces 3 qubits.
    Ordre des bases cohérent avec tes autres tests (qubit 0 = MSB)."""
    u = np.eye(8, dtype=Complex)
    # Échange |110> <-> |111> (indices 6 <-> 7)
    u[6, 6] = 0
    u[7, 7] = 0
    u[6, 7] = 1
    u[7, 6] = 1
    return u


TOFFOLI = Gate(_toffoli_3x3())
