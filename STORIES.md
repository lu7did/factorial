# STORIES

2025-10-29T23:56:42.859Z - Crear función factorial cumpliendo CONTEXT.md y armar esqueleto de proyecto (cookiecutter-like), tests, CI, docs, licencia MIT.
2025-10-30T00:03:14.401Z - Push al main con label "primer proyecto".
2025-10-30T00:06:59.749Z - Eliminar trufflehog como validación en cada push.
2025-10-30T00:08:25.331Z - Al pasar --n por argumento, calcular sin pedir entrada por teclado.
2025-10-30T00:10:35.804Z - Al informar --out y un nombre de archivo, se graba el resultado; caso contrario va a stdout.
2025-10-30T00:13:22.996Z - Actualizar CHANGELOG.md y README.md con todas las funciones; actualizar STORIES; push con label "funciones ok".
2025-10-30T00:14:24.683Z - Agregar test de integración cubriendo API y CLI (--n, --out, prompt por teclado).
2025-10-30T00:15:52.851Z - Correcciones para pasar Ruff: docstrings de módulos/funciones y configuración [tool.ruff.lint].
2025-10-30T00:20:17.672Z - Push al main con label "CI-OK".
2025-10-30T00:23:34.454Z - Corregir pytest agregando conftest.py para exponer src en sys.path.
2025-10-30T00:24:39.531Z - Push al main con label "CI-OK2".
2025-10-30T00:30:04.181114Z - Fix tests de integración (PYTHONPATH en subprocess).

2025-10-30T00:35:37.906000+00:00Z - Subir documentación generada con pdoc al repo (docs).
