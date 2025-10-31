from quantumsimulator.gate import Gate


class TestGate:

    def test_gate(self):
        gate = Gate.build([[1, 2], [3, 4]])
        assert gate * 2 == Gate.build([[2, 4],
                                       [6, 8]])
        assert 2 * gate == Gate.build([[2, 4],
                                       [6, 8]])
        assert gate / 2 == Gate.build([[1 / 2, 2 / 2],
                                       [3 / 2, 4 / 2]])
        gate2 = Gate.build([[5, 6],
                            [7, 8]])
        assert gate @ gate2 == Gate.build([[19, 22],
                                           [43, 50]])
        assert gate.__str__() == "[[1.+0.j 2.+0.j]\n [3.+0.j 4.+0.j]]"
        assert gate.__repr__() == "array([[1.+0.j, 2.+0.j],\n       [3.+0.j, 4.+0.j]])"
