#!/usr/bin/env python3

print("Example script python\n")


# Déclaration d'une function (def)
def my_function(arg1):
  print("Hello from a function\n")
  print(f"argument : {arg1}")

# Appel de la fonction
my_function("test d'argument")


# Déclartion d'une class  // constructeur(__init__)
class App:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def my_function(self, arg1):
      print("Hello from a class function\n")
      print(f"argument : {arg1}")

# Instance  de la class
inst = App(123, [])
print(inst.arg1, inst.arg2)
# Appel d'un function de la class
inst.my_function("234444")
