def escribir_lista_nombres():
    nombres = ["JoJo", "Dior", "V", "Jake", "Johnny Silverhand", "Dexter DeShawn", "Judy"]
    
    try:
        with open("/home/ub/Ejercicio de Python/Ej Archivos/Ej 4/nombres.txt", "w") as archivo:
            for nombre in nombres:
                archivo.write(nombre + "\n")
        return "Los nombres se han guardado correctamente en 'nombres.txt'."
    except PermissionError:
        return "Error: No tienes permiso para escribir en el directorio."
    except Exception as e:
        return f"Error inesperado: {e}"

print(escribir_lista_nombres())

try:
    with open("/home/ub/Ejercicio de Python/Ej Archivos/Ej 4/nombres.txt", "r") as archivo:
        print("\nContenido de 'nombres.txt' (verificación):")
        print(archivo.read())
except Exception:
    pass