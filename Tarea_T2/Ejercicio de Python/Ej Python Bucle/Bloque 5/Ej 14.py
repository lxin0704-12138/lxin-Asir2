suma = 0
print("Introduce números (ingresa 0 para terminar):")

while True:
    numero = float(input("Número: "))
    if numero == 0:
        break
    suma += numero

print(f"La suma de los números ingresados es: {suma:.2f}")
