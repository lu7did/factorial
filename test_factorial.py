#!/usr/bin/env python3
"""
Pruebas unitarias para el módulo factorial.
"""

import unittest
from factorial import factorial_iterativo, factorial_recursivo, factorial


class TestFactorial(unittest.TestCase):
    """Pruebas para las funciones de factorial"""
    
    def test_factorial_de_cero(self):
        """El factorial de 0 debe ser 1"""
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_recursivo(0), 1)
    
    def test_factorial_de_uno(self):
        """El factorial de 1 debe ser 1"""
        self.assertEqual(factorial_iterativo(1), 1)
        self.assertEqual(factorial_recursivo(1), 1)
    
    def test_factoriales_pequenos(self):
        """Prueba factoriales de números pequeños"""
        casos = [
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
        ]
        
        for n, esperado in casos:
            with self.subTest(n=n):
                self.assertEqual(factorial_iterativo(n), esperado)
                self.assertEqual(factorial_recursivo(n), esperado)
    
    def test_factoriales_grandes(self):
        """Prueba factoriales de números más grandes"""
        casos = [
            (10, 3628800),
            (15, 1307674368000),
            (20, 2432902008176640000),
        ]
        
        for n, esperado in casos:
            with self.subTest(n=n):
                self.assertEqual(factorial_iterativo(n), esperado)
                self.assertEqual(factorial_recursivo(n), esperado)
    
    def test_numero_negativo_genera_error(self):
        """El factorial de un número negativo debe generar ValueError"""
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)
        
        with self.assertRaises(ValueError):
            factorial_recursivo(-1)
        
        with self.assertRaises(ValueError):
            factorial_iterativo(-10)
        
        with self.assertRaises(ValueError):
            factorial_recursivo(-10)
    
    def test_no_entero_genera_error(self):
        """Pasar un no-entero debe generar TypeError"""
        valores_invalidos = [3.14, "5", [1, 2, 3], None, 2.0]
        
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    factorial_iterativo(valor)
                
                with self.assertRaises(TypeError):
                    factorial_recursivo(valor)
    
    def test_consistencia_entre_metodos(self):
        """Ambos métodos deben dar el mismo resultado"""
        for n in range(21):
            with self.subTest(n=n):
                self.assertEqual(
                    factorial_iterativo(n),
                    factorial_recursivo(n),
                    f"Los métodos difieren para n={n}"
                )
    
    def test_alias_factorial(self):
        """El alias 'factorial' debe funcionar"""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
