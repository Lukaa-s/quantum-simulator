from dataclasses import dataclass
import numpy as np

I2=np.identity(2)

class Register:
    n_qubits : int
    
    def __init__(self, n_qubits : int):
        self.n_qubits=n_qubits
        self.values=np.zeros(2**n_qubits,dtype=complex)
        #FIXME init with what ?



QubitIndex=int
class Gate1:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix=np.array(matrix_values)
    @staticmethod
    def tensor_power(matrix: np.ndarray,n:int)->np.ndarray:
        if n==0:
            return np.identity(np.size(matrix)[0])
        return np.tensordot(matrix,Gate1.tensor_power(matrix,n-1))
        

    def apply(self, register: Register, qubit_index: QubitIndex) -> Register:
        identity_before=Gate1.tensor_power(I2,qubit_index)
        identity_after=Gate1.tensor_power(I2,register.n_qubits-qubit_index-1)
        transform_matrix=np.tensordot(np.tensordot(identity_before,self.matrix),identity_after)
        return transform_matrix*register
    

H=Gate1([[1/np.sqrt(2),1/np.sqrt(2)],
         [1/np.sqrt(2),-1/np.sqrt(2)]])


