#  Guess the number
from random import *

nombre = input("Cual es tu nombre?: ")
intentos = 0
numero_ganador = randint(1,101)
numero_usuario = 0
print("\n")
print(f"Hola {nombre}, adivina el numero en que estoy pensando entre el 1 y el 100, tienes 8 intentos, mucha suerte")
print("\n")

while intentos < 8:
    numero_usuario = int(input("cual es el numero?: "))
    intentos += 1
    if numero_usuario not in range(1,101):
        print("Elige un numero entre 1 y 100")
    elif numero_usuario < numero_ganador:
        print("El numero ganador es mayor")
    elif numero_usuario > numero_ganador:
        print("El numero ganador es menor")
    else:
        print(f"Felicidades has ganado en {intentos} intentos")
        break
if numero_usuario != numero_ganador:
    print(f"Lo siento has perdido, el numero ganador era {numero_ganador}")