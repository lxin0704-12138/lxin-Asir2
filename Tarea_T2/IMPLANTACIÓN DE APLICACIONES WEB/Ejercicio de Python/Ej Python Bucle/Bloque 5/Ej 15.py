numero = 5
factorial = 1

if numero < 0:
    print("El factorial no existe para num nagativos.")
elif numero == 0 or numero == 1:
    print(f"El factorial de {numero} es 1")
else:
    contador = numero
    while contador > 1:
        factorial *= contador
        contador -= 1
        print(f"El factoral de {numero} es {factorial}")