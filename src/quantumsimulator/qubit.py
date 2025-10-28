from dataclasses import dataclass
from typing import Literal, Union
from numpy import  round, abs
from numpy.random import random

ZeroType = Literal[0]
OneType = Literal[1]

ZERO: ZeroType = 0
ONE: OneType = 1

MeasureResult = Union[ZeroType, OneType]


@dataclass(frozen=True)
class Qubit: 
    alpha: complex # coefficient for |0>
    beta: complex # coefficient for |1>

    # FIXME guarantee module 1

    def measure(self) -> MeasureResult:
        if random()<=abs(self.alpha)**2:
            return ZERO
        else:
            return ONE

    def arg(self) -> float:
        pass
    

QBIT0 = Qubit(1, 0)
QBIT1 = Qubit(0, 1)
