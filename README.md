# factorial-pkg

Versión 1.0 build 009

Paquete Python 3.12 para calcular el factorial cumpliendo CONTEXT.md. Incluye API, CLI, tests, CI y documentación.

Uso de librería:
- from factorial_pkg import factorial
- factorial(5) -> 120

Uso de CLI:
- python -m factorial_pkg --n 5
- factorial --n 5
- Para escribir en archivo: python -m factorial_pkg --n 5 --out resultado.txt
- Si no se especifica --n, el programa solicitará el valor por teclado.
- Si no se especifica --out, el resultado se imprime por salida estándar.

Directorios scripts/ y ejemplos/ no se incluyen en el workflow de validación.

## Funciones disponibles

- API:
  - factorial(n: int) -> int: devuelve n!.
  - FactorialCalculator.compute(n: int) -> int: devuelve n!.
- CLI:
  - --n: número entero n >= 0.
  - --out: archivo donde escribir el resultado; si no se indica, imprime por stdout.
