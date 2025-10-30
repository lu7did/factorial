"""Configura sys.path para incluir el directorio 'src' durante los tests."""

from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
if SRC.exists():  # pragma: no cover
    sys.path.insert(0, str(SRC))
