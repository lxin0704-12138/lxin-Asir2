cadena = "Python es genial"
vocales = ["a", "e", "i", "o", "u"]
contador = 0

for letra in cadena.lower():
    if letra in vocales:
        contador += 1

print(f"La cadena contiene {contador} vocales.")