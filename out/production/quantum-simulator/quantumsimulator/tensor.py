import numpy as np

from quantumsimulator.types import CArray


class Tensor:

    @staticmethod
    def power(self, n: int, matrix: CArray) -> CArray:
        if n == 0:
            return np.identity(np.size(matrix)[0])
        return np.tensordot(matrix, self.power(n - 1, matrix))
