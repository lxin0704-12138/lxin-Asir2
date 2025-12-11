def buscar_palabra_archivo():
    palabra_buscada = input("Introduce la palabra a buscar: ").strip()
    if not palabra_buscada:
        return "Error: No introdujiste ninguna palabra."
    
    contador = 0
    try:
        with open("/home/ub/Ejercicio de Python/Ej Archivos/Ej 3/articulo.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                contador += linea.lower().count(palabra_buscada.lower())
        return f"La palabra '{palabra_buscada}' aparece {contador} veces en 'articulo.txt'."
    except FileNotFoundError:
        return "Error: El archivo 'articulo.txt' no existe."
    except Exception as e:
        return f"Error inesperado: {e}"

print(buscar_palabra_archivo())