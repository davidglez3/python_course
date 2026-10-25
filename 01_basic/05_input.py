### 
# 05 - Entrada de usuario (input()) - versión simlpificada
# La función input() permite obtener datos del usuario a través de la consola.
###

print("¿Como te llamas?")
nombre: str = input()

# Podemos hacer así el input directamente
apellido: str = input("Como es tu apellido?")

# Podemos añadir un salto de línea al input para que la respuesta vaya en otra, sino lo pone a continuación
apellido2: str = input("Como es tu apellido?\n")

print(f"Hola {nombre} {apellido} {apellido2}, encantado de conocerte")

age: int = int(input("Cuantos años tienes?\n"))

print(f"Dentro de 20 años tendrás {age + 20} años") # Hay que pasarlo a int ya que al leer de input siempre es str

print("Obtener varios valores a la vez")
country, city = input("En que país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")