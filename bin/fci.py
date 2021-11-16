#!/usr/bin/env python3
#from lib.library import diviseInteger, addInteger, multipliInteger
from lib.rectangle import CalculAireRectangle, CalculPerimetreRectangle,mafunction

# les tests

# a = 2
# b = 4
# result = addInteger(a, b)
# print(f"Le resultat de {a} + {b} est : {result}")
#
# result = multipliInteger(a, b)
# print(f"Le resultat de {a} + {b} est : {result}")
#
# result = diviseInteger(a, b)
# print(f"Le resultat de {a} + {b} est : {result}")

longueur = 18
largeur = 14
result = CalculAireRectangle(longueur,largeur)
print(f"Le resultat aire du rectangle de longueur {longueur} largueur  {largeur} est : {result}")


result = CalculPerimetreRectangle(longueur,largeur)
print(f"Le resultat perimetre du rectangle de longueur {longueur} largueur  {largeur} est : {result}")

result = CalculPerimetreRectangle("33","123")
print(f"Le resultat perimetre du rectangle de longueur 33 largueur 123 est : {result}")

result = mafunction (13,17,"cci")
print (result)
