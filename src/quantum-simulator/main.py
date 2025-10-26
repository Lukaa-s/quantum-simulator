from gate import *
from qubit import *

print("Quantum Simulator")

qubit = Qubit(0, 1)
print(qubit.measure())
result = H.apply(qubit)

print(result)
