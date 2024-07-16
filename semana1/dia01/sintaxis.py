#Comentario en una sola linea
"""
Comentario en varias lineas
se realiza con triple comilla doble
"""

"""Imprimir en pantalla"""
print("Hola mundo")

"""Variables"""
numero = 10

"""Identacion"""
def suma(a,b):
  def division(a,b):
    return a/b
  return a + b

"""Condicionales"""
if numero>10:
  print("mayor a 10")
elif numero == 10:
  print("numero es igual a 10")
else:
  print("menor o igual a 10")

"""Condicionales con operadores logicos"""
if numero > 10 and numero < 20:
  print("mayor a 10 y menor a 20")

if numero > 10 or numero < 20:
  print("mayor a 10 o menor a 20")
