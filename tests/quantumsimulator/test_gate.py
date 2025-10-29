import pytest
import numpy as np
from quantumsimulator.gates import H, SQRT_2, CNOT, I, X, Y, Z, Gate_n
from quantumsimulator.register import Register


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

class TestGate:

    @pytest.mark.parametrize("label,right,left", [
        ("I ** 2 == I", I ** 2, I),
        ("X ** 2 == I", X ** 2, I),
        ("Y ** 2 == I", Y ** 2, I),
        ("Z ** 2 == I", Z ** 2, I),
        ("-1j * X @ Y @ Z == I", -1j * X @ Y @ Z, I),
        ("Z @ X == 1j * Y", Z @ X, 1j * Y),
        ("1j * Y == -1 * X @ Z", 1j * Y, -1 * X @ Z),
    ])
    def test_gates(self, label, right, left):
        assert right == left, label

    def test_gate_H(self):
        register_input = Register(1)
        register_input.set_value(0, 0)
        register_input.set_value(1, 1)
        register_output = H.apply(register_input, [0])
        assert register_output.get_value(0) == 1 / SQRT_2, "wrong H 0 result"
        assert register_output.get_value(1) == -1 / SQRT_2, "wrong H 1 result"

    def test_gate_CNOT(self):
        register_input = Register(2)
        register_input.set_value(0, 0)
        register_input.set_value(1, 1)
        register_input.set_value(2, 1)
        register_input.set_value(3, 0)
        register_output = CNOT.apply(register_input, [0, 1])
        assert register_output.get_value(0) == 0, "wrong H 0 result"
        assert register_output.get_value(1) == 1 + 0j, "wrong H 1 result"
        assert register_output.get_value(2) == 0, "wrong H 2 result"
        assert register_output.get_value(3) == 1 + 0j, "wrong H 3 result"

    @pytest.mark.parametrize("input,expected", [
        ([+1, +1, +1, +1], [+1, +1, +1, +1]),
        ([+1, -1, +1, -1], [+1, -1, -1, +1]),
        ([+1, +1, -1, -1], [+1, +1, -1, -1]),
        ([+1, -1, -1, +1], [+1, -1, +1, -1]),
    ])
    def test_gate_CNOT_real(self, input, expected):
        register_input = Register(2)
        for idx in range(4):
            register_input.set_value(idx, input[idx] * 0.5)
        register_output = CNOT.apply(register_input, [0, 1])
        for idx in range(4):
            assert register_output.get_value(idx) == expected[idx] * 0.5, f"wrong CNOT result {idx}"


    
def test_gate_3qubits_on_4qubits_basic():
    # État initial = |1100> (qubits: q0 q1 q2 q3 ; q0=MSB)
    reg = Register(4)
    reg.set_value(12, 1.0 + 0j)  # 0b1100 = 12

    TOFFOLI = Gate_n(toffoli_3x3())

    # Appliquer la porte 3-qubits sur [0,1,2] (les 3 qubits de gauche)
    out = TOFFOLI.apply(reg, [0, 1, 2])

    # Toffoli doit flipper q2 (0->1) puisque q0=q1=1, et laisser q3 inchangé (=0)
    # Donc |1100> -> |1110>  (index 12 -> 14)
    for idx in range(16):
        expected = 1.0 + 0j if idx == 14 else 0.0 + 0j
        assert out.get_value(idx) == expected, f"mauvaise amplitude à l'index {idx}"
        
def test_gate_3qubits_on_4qubits_controls_not_satisfied():
    # État initial = |1000> : un seul contrôle à 1 → Toffoli ne fait rien
    reg = Register(4)
    reg.set_value(8, 1.0 + 0j)   # 0b1000 = 8

    TOFFOLI = Gate_n(toffoli_3x3())
    out = TOFFOLI.apply(reg, [0, 1, 2])

    # Doit rester |1000> (index 8)
    for idx in range(16):
        expected = 1.0 + 0j if idx == 8 else 0.0 + 0j
        assert out.get_value(idx) == expected, f"la Toffoli a modifié un état sans contrôler=11 (index {idx})"