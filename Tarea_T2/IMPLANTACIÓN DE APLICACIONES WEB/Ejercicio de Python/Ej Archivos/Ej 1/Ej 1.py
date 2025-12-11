try:
    with open("/home/ub/Ejercicio de Python/Ej Archivos/Ej 1/notas.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido de notas.txt:")
        print("-" * 30)
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo 'notas.txt' no existe en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")