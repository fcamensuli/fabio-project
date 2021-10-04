#!/usr/bin/env python3


def addInteger(x, y):
    if type (x) == "str":
        x = int(x)

    if type (y) == "str":
        y = int(y)

    return (x + y)

def multipliInteger(x, y):
    if type (x) == "str":
        x = int(x);

    if type (y) == "str":
        y = int(y)

    return (x * y)


def diviseInteger(x, y):
    if y == 0:
        error =  "la divion par 0 est interdite"
        raise NameError(error)

    if type (x) == "str":
        x = int(x)

    if type (y) == "str":
        y = int(y)

    return (x / y)


# les tests

a = 2
b = 0
result = addInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")

result = multipliInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")


result = diviseInteger(a, b)
print(f"Le resultat de {a} + {b} est : {result}")
