###
# 01 - Sentencias condicioneales (if, elif, else)
# Pedrmiten ejecutar bloques de código si se cumplen ciertas condiciones
###

###
# Función que nos permite limpiar la terminal, si es windows ejecuta una shell con cls y si no clear.
###
import os
import subprocess

def limpiar_pantalla():
    if os.name == "nt":
        subprocess.run("cls",shell=True)
    else:
        subprocess.run(["clear"])

limpiar_pantalla()

print("\n Sentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")


print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 7
if nota >= 9:
    print("Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("Aprobado!")
else:
    print("No está calificado")


print("\n Condiciones múltiples")
edad = 17
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("A la cárcel")


if edad > 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Paga a la policía y te deja conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("A estudiar")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad > 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

if edad > 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quédate en casa")


print("\nLa condición ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condición] else [código si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad > 18 else "Es menor de edad"
print(mensaje)