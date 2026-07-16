# quantum-simulator

A small quantum computing simulator written in Python from scratch (state vectors and matrices, no quantum SDK). It implements the gate model on top of NumPy and includes a working version of Grover's search algorithm.

## What it does

- `Register` (`src/quantumsimulator/register.py`): a state vector of `2**n` complex amplitudes for an n-qubit system.
- `Gate` (`src/quantumsimulator/gate.py`): builds a unitary matrix from raw values and applies it to any subset of qubits in a register. Applying a gate to qubits that aren't the last ones in the register is done by building a permutation matrix and conjugating the gate's Kronecker-expanded matrix with it, so a gate can be applied to any qubit position without special-casing.
- `gates.py`: the standard set built on top of `Gate`: H, X (aliased as NOT), Y, Z, S, T, CNOT, and Toffoli (CCNOT).
- `Operator` and `operators.py`: n-qubit unitary operators applied directly to a register's amplitude vector, used for the search oracle and for the CZ diffuser step.
- `Grover` (`src/quantumsimulator/algorithm.py`): a full implementation of Grover's search algorithm. It prepares the uniform superposition with Hadamards, then runs `floor(pi/4 * sqrt(2**n))` iterations of oracle + diffusion (H, X, CZ, X, H), asserting the state vector stays normalized after every step.

There is no CLI or notebook demo; the project is exercised entirely through pytest, and Grover is called directly from Python as shown below.

## Run it

Requires Python 3.13 (declared in `pyproject.toml`); it also runs fine under 3.12 in practice.

With Poetry (as documented in `DEV.md`):

```shell
poetry install
eval $(poetry env activate)   # bash/zsh; PowerShell: Invoke-Expression (poetry env activate)
pytest tests
```

Without Poetry, plain pip works too:

```shell
pip install numpy pytest
PYTHONPATH=src pytest tests
```

Both give the same result, verified on this repo:

```
22 passed in 0.33s
```

### Running Grover directly

There's no bundled script, but the algorithm is easy to call from a Python shell. Example: search a 2-qubit register (4 states) for `|10>` using a phase-flip oracle:

```python
import numpy as np
from quantumsimulator.algorithm import Grover
from quantumsimulator.operator import Operator
from quantumsimulator.types import Complex

n = 2
u = np.identity(2 ** n, dtype=Complex)
u[2, 2] = -1          # phase-flip oracle marking |10> (index 2)
oracle = Operator(n, u)

result = Grover.run(n, oracle)
probs = np.abs(result.values) ** 2
print(probs, np.argmax(probs))
```

Verified output:

```
[9.07105347e-35 0.00000000e+00 1.00000000e+00 0.00000000e+00] 2
```

Grover converges to the marked state (index 2) with probability ~1 in a single iteration, since `floor(pi/4 * sqrt(4)) = 1`.

## Possible next steps

- No measurement operation: `Register` exposes raw amplitudes (`get_value`, `norm`) but there's no method to sample a basis state from the probability distribution.
- Only Grover is implemented; other textbook algorithms (QFT, phase estimation) would reuse the same `Gate`/`Operator`/`Register` building blocks.
- Still no test covers `T` or `S` directly (only their relations to other gates, via `test_gates.py`); a direct unitarity/value check for each single-qubit gate would catch regressions like the one fixed below.

Note: `T` used to be defined as `diag(1, sqrt(2)/2)`, which is not unitary (`T^dagger @ T != I`). It's now `diag(1, exp(i*pi/4))`, verified unitary within tolerance.
