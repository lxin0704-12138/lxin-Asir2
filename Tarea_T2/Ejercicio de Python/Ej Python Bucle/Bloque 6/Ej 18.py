import random

numero_secreto = random.randint(1, 20)
print("Adivina el número secreto (1-20). Escribe 'salir' para terminar.")

while True:
    entrada = input("(๑・̀ㅂ・́)و✧Good luck!! Intento: ")
    
    if entrada.lower() == "salir":
        print(f"!_!Game Over!O.o! El num secreto era {numero_secreto}.")
        break
    
    if not entrada.isdigit():
        print("Por favor, introduce un num válido o 'salir'.")
        continue
    
    intento = int(entrada)
    
    if intento == numero_secreto:
        print("Felicidades!(≧∇≦)! Adivinaste el numero secreto!")
        break
    elif intento < numero_secreto:
        print("El numero secreto es mayor. Intenta de nuevo.")
    else:
        print("El numero secreto es menor. Intenta de nuevo.")