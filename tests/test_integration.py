import sys
import subprocess
from pathlib import Path

from factorial_pkg import factorial, FactorialCalculator


def run_cli(args: list[str], input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "factorial_pkg", *args],
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_stdout() -> None:
    proc = run_cli(["--n", "6"])  # 6! = 720
    assert proc.returncode == 0
    assert proc.stderr == ""
    assert proc.stdout.strip().splitlines()[-1] == "720"


def test_cli_out_file(tmp_path: Path) -> None:
    out = tmp_path / "resultado.txt"
    proc = run_cli(["--n", "7", "--out", str(out)])  # 7! = 5040
    assert proc.returncode == 0
    assert proc.stderr == ""
    # Cuando se usa --out no debe imprimir por stdout
    assert proc.stdout == ""
    assert out.read_text(encoding="utf-8").strip() == "5040"


def test_cli_prompt_from_stdin() -> None:
    proc = run_cli([], input_text="4\n")  # 4! = 24
    assert proc.returncode == 0
    # La primera línea puede contener el prompt; el resultado debe ser la última línea
    assert proc.stdout.strip().splitlines()[-1] == "24"


def test_api_and_oop() -> None:
    assert factorial(5) == 120
    assert FactorialCalculator().compute(5) == 120
