from quantumsimulator.register import Register


class TestRegister:

    def test_register(self):
        reg = Register(2)
        assert reg.n_qubits == 2
        assert len(reg.values) == 4  # 2^2 = 4 states
