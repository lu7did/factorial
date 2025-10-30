"""Tests para factorial_pkg."""

import subprocess
import sys
from pathlib import Path

from factorial_pkg import FactorialCalculator, factorial


def run_cli(args: list[str], input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    """Ejecuta la CLI y retorna el proceso completado."""
    return subprocess.run(
        [sys.executable, "-m", "factorial_pkg", *args],
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_stdout() -> None:
    """Prueba de integración."""
    proc = run_cli(["--n", "6"])  # 6! = 720
    assert proc.returncode == 0
    assert proc.stderr == ""
    assert proc.stdout.strip().splitlines()[-1] == "720"


def test_cli_out_file(tmp_path: Path) -> None:
    """Prueba de integración."""
    out = tmp_path / "resultado.txt"
    proc = run_cli(["--n", "7", "--out", str(out)])  # 7! = 5040
    assert proc.returncode == 0
    assert proc.stderr == ""
    # Cuando se usa --out no debe imprimir por stdout
    assert proc.stdout == ""
    assert out.read_text(encoding="utf-8").strip() == "5040"


def test_cli_prompt_from_stdin() -> None:
    """Prueba de integración."""
    proc = run_cli([], input_text="4\n")  # 4! = 24
    assert proc.returncode == 0
    # El resultado debe ser el último token de la última línea (puede incluir el prompt)
    last_line = proc.stdout.strip().splitlines()[-1]
    assert last_line.split()[-1] == "24"


def test_api_and_oop() -> None:
    """Prueba de integración."""
    assert factorial(5) == 120
    assert FactorialCalculator().compute(5) == 120
