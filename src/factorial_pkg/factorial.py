"""Funciones para cálculo de factorial."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FactorialCalculator:
    """Strategy-like calculator for factorial computation."""

    def compute(self, n: int) -> int:
        """Compute n! for n >= 0.

        Raises ValueError for negative n and TypeError for non-integers.
        """
        return factorial(n)


def factorial(n: int) -> int:
    """Return the factorial of n (n >= 0).

    Raises
    ------
    TypeError
        If n is not an int.
    ValueError
        If n is negative.

    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    # Iterative multiplication to avoid recursion overhead and depth limits.
    for k in range(2, n + 1):
        result *= k
    return result
