import numpy as np

from quantumsimulator.gate import Gate

SQRT_2 = np.sqrt(2)

H = Gate([[1, 1],
          [1, -1]]) / SQRT_2
I = Gate([[1, 0],
          [0, 1]])
X = Gate([[0, 1],
          [1, 0]])
NOT = X
Y = Gate([[0, -1j],
          [1j, 0]])
Z = Gate([[1, 0],
          [0, -1]])
S = Gate([[1, 0],
          [0, -1j]])
T = Gate([[1, 0],
          [0, SQRT_2 / 2]])

CNOT = Gate([[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 1],
             [0, 0, 1, 0],
             ])


def toffoli_3x3():
    """Matrice 8x8 de la Toffoli (CCNOT) avec contrôles sur les deux bits
    les plus significatifs et cible = bit le moins significatif de ces 3 qubits.
    Ordre des bases cohérent avec tes autres tests (qubit 0 = MSB)."""
    U = np.eye(8, dtype=complex)
    # Échange |110> <-> |111> (indices 6 <-> 7)
    U[6, 6] = 0
    U[7, 7] = 0
    U[6, 7] = 1
    U[7, 6] = 1
    return U


TOFFOLI = Gate.init(toffoli_3x3())
