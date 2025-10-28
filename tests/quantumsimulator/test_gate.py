import pytest

from quantumsimulator.register import Register, H, SQRT_2, CNOT


class TestGate:

    def test_gate_H(self):
        register_input = Register(1)
        register_input.set_value(0, 0)
        register_input.set_value(1, 1)
        register_output = H.apply(register_input, 0)
        assert register_output.get_value(0) == 1 / SQRT_2, "wrong H 0 result"
        assert register_output.get_value(1) == -1 / SQRT_2, "wrong H 1 result"

    def test_gate_CNOT(self):
        register_input = Register(2)
        register_input.set_value(0, 0)
        register_input.set_value(1, 1)
        register_input.set_value(2, 1)
        register_input.set_value(3, 0)
        register_output = CNOT.apply(register_input,[0,1])
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
        register_output = CNOT.apply(register_input,[0,1])
        for idx in range(4):
            assert register_output.get_value(idx) == expected[idx] * 0.5, f"wrong CNOT result {idx}"
