from __future__ import annotations

import argparse
import sys

from .factorial import FactorialCalculator


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(prog="factorial", description="Calcula n! (n factorial).")
    parser.add_argument("n", type=int, help="Número entero n >= 0")
    args = parser.parse_args()

    try:
        calc = FactorialCalculator()
        value = calc.compute(args.n)
        print(value)
    except Exception as exc:  # pragma: no cover - stderr path
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
