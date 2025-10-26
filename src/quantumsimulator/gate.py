from dataclasses import dataclass

import numpy as np

from quantumsimulator.qubit import Qubit


class Gate:
    pass


@dataclass(frozen=True)
class Gate1(Gate):
    matrix: np.ndarray

    def apply(self, qubit: Qubit) -> Qubit:
        vector = self.matrix @ np.array([[qubit.alpha], [qubit.beta]])
        return Qubit(vector[0][0], vector[1][0])


@dataclass(frozen=True)
class Gate2(Gate):
    def apply(self, qubit1: Qubit, qubit2: Qubit) -> Qubit:
        pass


SQRT_2 = np.sqrt(2)
H = Gate1(np.array([[1, 1], [1, -1]]) / SQRT_2)
