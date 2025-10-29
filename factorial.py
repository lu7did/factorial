#!/usr/bin/env python3
"""
Módulo para calcular el factorial de un número.

Este módulo proporciona diferentes implementaciones para calcular
el factorial de un número entero no negativo.
"""


def factorial_iterativo(n):
    """
    Calcula el factorial de n usando un enfoque iterativo.
    
    Args:
        n (int): Un número entero no negativo
        
    Returns:
        int: El factorial de n
        
    Raises:
        ValueError: Si n es negativo
        TypeError: Si n no es un entero
    
    Ejemplos:
        >>> factorial_iterativo(0)
        1
        >>> factorial_iterativo(5)
        120
        >>> factorial_iterativo(10)
        3628800
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un número entero")
    
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado


def factorial_recursivo(n):
    """
    Calcula el factorial de n usando un enfoque recursivo.
    
    Args:
        n (int): Un número entero no negativo
        
    Returns:
        int: El factorial de n
        
    Raises:
        ValueError: Si n es negativo
        TypeError: Si n no es un entero
    
    Ejemplos:
        >>> factorial_recursivo(0)
        1
        >>> factorial_recursivo(5)
        120
        >>> factorial_recursivo(10)
        3628800
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un número entero")
    
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)


# Alias para facilitar el uso
factorial = factorial_iterativo


if __name__ == "__main__":
    # Ejemplos de uso
    print("Demostración del cálculo de factoriales")
    print("=" * 40)
    
    for i in range(11):
        print(f"factorial({i}) = {factorial(i)}")
    
    print("\nComparación de métodos:")
    n = 10
    print(f"Iterativo: factorial({n}) = {factorial_iterativo(n)}")
    print(f"Recursivo: factorial({n}) = {factorial_recursivo(n)}")
