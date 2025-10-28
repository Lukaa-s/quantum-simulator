import numpy as np

class Tensor:

    @staticmethod
    def power(self, n:int, matrix: np.ndarray) -> np.ndarray:
        if n==0:
            return np.identity(np.size(matrix)[0])
        return np.tensordot(matrix,self.power(n-1,matrix))