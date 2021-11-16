#  rectangle

def CalculAireRectangle(longueur, largeur):
  if type(longueur) == str:
    longueur = int(longueur)
  if type(largeur) == str:
    largeur = int(largeur)
  return (largeur * largeur)


def CalculPerimetreRectangle(longueur, largeur):
  print(longueur, largeur)
  if type(longueur) == str:
    longueur = int(longueur)
  if type(largeur) == str:
    largeur = int(largeur)
  return ((largeur + largeur) * 2)


def mafunction(val1, val2, val3):
  print(val1, val2, val3)
  return val1 + val2
