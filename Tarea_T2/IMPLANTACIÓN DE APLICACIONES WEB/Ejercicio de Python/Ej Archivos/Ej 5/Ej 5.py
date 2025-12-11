def copiar_archivo():
    origen = "/home/ub/Ejercicio de Python/Ej Archivos/Ej 5/origen.txt"
    destino = "/home/ub/Ejercicio de Python/Ej Archivos/Ej 5/destino.txt"
    
    try:
        with open(origen, "r", encoding="utf-8") as archivo_origen:
            contenido = archivo_origen.read()

        with open(destino, "w", encoding="utf-8") as archivo_destino:
            archivo_destino.write(contenido)
        
        return f"Éxito: Contenido de '{origen}' copiado a '{destino}'."
    except FileNotFoundError:
        return f"Error: El archivo '{origen}' no existe."
    except Exception as e:
        return f"Error inesperado: {e}"

print(copiar_archivo())