"""Tests para factorial_pkg."""

import pytest

from factorial_pkg import FactorialCalculator, factorial


@pytest.mark.parametrize(
    "n,expected",
    [(0, 1), (1, 1), (2, 2), (3, 6), (5, 120), (10, 3628800)],
)
def test_factorial_values(n: int, expected: int) -> None:
    """Prueba de integración."""
    assert factorial(n) == expected
    assert FactorialCalculator().compute(n) == expected


def test_factorial_negative_raises() -> None:
    """Prueba de integración."""
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_type_error() -> None:
    """Prueba de integración."""
    with pytest.raises(TypeError):
        factorial(3.5)  # type: ignore[arg-type]
