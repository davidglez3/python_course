### 
# 02 - Booleanos
# Valores lógicos: True (Verdadero) y False (falso)
# Fundamentales para el control de flujo y la lógica en programación
###

import os
import subprocess
def limpiar_pantalla():
    if os.name == "nt":
        subprocess.run("cls",shell=True)
    else:
        subprocess.run(["clear"])

# Los booleanos representan valores de verdad: True o False
print("\nValores booleanos básicos:")
print(True)
print(False)


# Operadores de comparación: devuelven un valor booleano.
print("6 > 2:", 6 > 2)          # True
print("6 < 2:", 6 < 2)          # False
print("5 == 5:", 5 == 5)        # True (igualdad)
print("5 != 3:", 5 != 3)        # True (desigualdad)
print("5 >= 5:", 5 >= 5)        # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)        # False (menor o igual que)

limpiar_pantalla()

print("\nComparacíón de cadenas:")
print("manzana < pera:","manzana" < "pera") # True
print("'Hola' == 'hola'", "Hola" == "hola") #False

# Operadores lógicos
print("\nOperadores lógicos:")
print("True and True:", True and True )         # True
print("True and False:", True and False)         # False
print("False or False:", False or False)         # False
print("not True:", not True)                     # False
print("not False:", not False)                   # True