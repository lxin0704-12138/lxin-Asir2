def contar_lineas_archivo(nombre_archivo):
    contador = 0
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for _ in archivo:
                contador += 1
        return contador
    except FileNotFoundError:
        return f"Error: El archivo '{nombre_archivo}' no existe."
    except Exception as e:
        return f"Error inesperado: {e}"

resultado = contar_lineas_archivo("/home/ub/Ejercicio de Python/Ej Archivos/Ej 2/poema.txt")
if isinstance(resultado, int):
    print(f"El archivo 'poema.txt' tiene {resultado} líneas.")
else:
    print(resultado)