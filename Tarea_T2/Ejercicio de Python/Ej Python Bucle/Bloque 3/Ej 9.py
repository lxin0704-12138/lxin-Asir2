cadena = "Hola a todos"
cadena_sin_espacios = ""

for letra in cadena:
    if letra != " ":
        cadena_sin_espacios += letra

print(f"Cadena sin espacios: {cadena_sin_espacios}")