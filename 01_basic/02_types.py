###
# 01 - ptypes()
# Python tiene varios tipos de datos
# int, float, str,bool, NoneType, list, tuple, dict, range, set...
###

"""
    Así puedes hacer una cadena de texto multilínea y si no lo asignas a nada.....
    Se trata de un comentario
"""

print ("int:")
print(type(10))
print(type(0))
print(type(-5))
print(type(15641314546564616485415634))

print("float:")
print(type(3.14))
print(type(1.0))
print(type(1e3)) #1000.0

print("complex:")
print(type(1 + 2j))

print("str:")
print(type("hola"))
print(type(""))
print(type("1346"))
print(type("""
    Multilinea
"""))

print("Bool:")
print(type(True))
print(type(False))
print(type(1 < 2))

print("NonType:")
print(type(None)) #Se usa para la ausencia de valor