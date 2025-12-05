numeros = [10, 15, 20, 25, 30]
numeros_pares = []

for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)

print(f"Numeros pares: {numeros_pares}")