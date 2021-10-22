#!/usr/bin/env python3
from lib.library import diviseInteger, addInteger, multipliInteger

# les tests

a = 2
b = 4
result = addInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")

result = multipliInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")

result = diviseInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")
