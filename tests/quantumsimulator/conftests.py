# tests/conftest.py
import os, sys

# Racine du repo (…/quantum-simulator)
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(REPO, "src")

# On met SRC en tout premier pour prioriser ton vrai package
for p in (SRC, REPO):
    if p not in sys.path:
        sys.path.insert(0, p)

# Petit sanity-check (facultatif mais utile au début)
try:
    import quantumsimulator  # noqa: F401
except Exception as e:
    raise RuntimeError(
        f"Impossible d'importer le package 'quantumsimulator'. "
        f"Attendu sous {SRC}\\quantumsimulator. Détails: {e}"
    )
