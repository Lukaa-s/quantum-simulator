from dataclasses import dataclass
from typing import Literal, Union

ZeroType = Literal[0]
OneType = Literal[1]

ZERO: ZeroType = 0
ONE: OneType = 1

type MeasureResult = Union[ZeroType, OneType]


@dataclass(frozen=True)
class Qubit:
    alpha: complex
    beta: complex

    # FIXME guarantee module 1
    def measure(self) -> MeasureResult:
        pass

    def arg(self) -> float:
        pass
    

QBIT0 = Qubit(1, 0)
QBIT1 = Qubit(0, 1)
