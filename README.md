# Calculadora de Factorial

Demo de vibe coding para el cálculo de un factorial de números enteros no negativos.

## Descripción

Este proyecto implementa el cálculo del factorial de un número entero usando dos enfoques diferentes:
- **Iterativo**: Usa un bucle for para calcular el factorial
- **Recursivo**: Usa recursión para calcular el factorial

## Requisitos

- Python 3.6 o superior

## Uso

### Como módulo

```python
from factorial import factorial, factorial_iterativo, factorial_recursivo

# Usando la función por defecto (iterativa)
resultado = factorial(5)  # 120

# Usando explícitamente el método iterativo
resultado = factorial_iterativo(10)  # 3628800

# Usando el método recursivo
resultado = factorial_recursivo(7)  # 5040
```

### Desde la línea de comandos

```bash
python3 factorial.py
```

Este comando ejecutará una demostración que muestra el factorial de los números del 0 al 10.

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
python3 test_factorial.py
```

Las pruebas cubren:
- Casos base (0! = 1, 1! = 1)
- Factoriales pequeños (2! hasta 7!)
- Factoriales grandes (hasta 20!)
- Validación de errores (números negativos, tipos incorrectos)
- Consistencia entre métodos iterativo y recursivo

## Ejemplos

```python
factorial(0)   # 1
factorial(1)   # 1
factorial(5)   # 120
factorial(10)  # 3628800
```

## Definición Matemática

El factorial de un número entero no negativo n, denotado como n!, se define como:

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

Con casos especiales:
- 0! = 1
- 1! = 1

## Licencia

MIT License - Ver archivo LICENSE para más detalles.
