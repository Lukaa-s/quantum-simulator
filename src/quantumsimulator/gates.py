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
