###
# 04 - Variables
# Las variables sirven para fuarfar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###

# Para asignar una palpabra únicamente es necesario poner el nombre
my_name = "David"

print(my_name)

age = 32
print(age)

# Las variables se pueden reasignar en tiempo de ejecución
age = 39
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# No tienes que declaralo explícitamente
name = "David"
print(type(name))

name = 32
print(type(name))

# Es de tipado fuerte: Python  no realiza conversiones de tipo automático
# print(10 + "2") esto no lo suma, da error ya que son dos tipos distintos

# f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age} años")

# No recomendada forma de asignar variables
name, age, city = "David", 32, "Pola de Lena"

# Convenciones de nombres de varibales
mi_nombre_de_variable = "Ok" # Snake case
MI_CONSTANTE = 3.14 # UPPER_CASE -> constante

# No debería hacerse así
MiNombreDeVariable = "Ko" # PascalCase
minombredevariable = "Ko"

# Nombres no válidos de variables
# 1234_variable = "Ko"
# mi-varibale = "Ko"
# mi variable = "Ko"
#
# Palabras reservadas:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 
# 'with', 'yield']


# Types anotation, podemos indicar de que tipo será la variable pero eso no restringe que se utilice para otro tipo de dato. Serviría como comentario
is_user_logged_in: bool = True #Aqui le añadimos la anotación que es un booleano
print(is_user_logged_in)

is_user_logged_in = 32 #Aqui vemos que podemos cambiar sin problema a int, aunque tenga la anotación de bool
print(is_user_logged_in)

