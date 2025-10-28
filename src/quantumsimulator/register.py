from dataclasses import dataclass
import numpy as np
from quantumsimulator.tensor import Tensor
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


    def apply(self, register: Register, qubit_index: QubitIndex) -> Register:
        identity_before=Tensor.power(I2,qubit_index)
        identity_after=Tensor.power(I2,register.n_qubits-qubit_index-1)
        transform_matrix=np.tensordot(np.tensordot(identity_before,self.matrix),identity_after)
        return transform_matrix*register
    

H=Gate1([[1/np.sqrt(2),1/np.sqrt(2)],
         [1/np.sqrt(2),-1/np.sqrt(2)]])


class Gate2:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix=np.array(matrix_values)
        
    def apply(self, register: Register, qubit_index1: QubitIndex, qubit_index2: QubitIndex) -> Register:
        pass
class Gate_n:
    def __init__(self, matrix_values: list[list[complex]]):
        self.matrix=np.array(matrix_values)
        
    def apply(self, register: Register, qubit_indices: list[QubitIndex]) -> Register:
        u=self.matrix
        qubit_positions=[k for k in range(register.n_qubits)]
        swaps={}
        for i in qubit_indices:
            if qubit_indices[i]!=i:
                #swap qubit i and qubit_indices[i]
                swaps[i]=qubit_indices[qubit_positions[i]]
                temp=qubit_positions[i]
                qubit_positions[i]=qubit_positions[qubit_indices[i]] #swap
                qubit_positions[qubit_indices[i]]=temp  
        #update matrix

        return u*register
        
        
        
        
    
