def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    print("-" * 20)

imprimir_detalles(nombre="JoJo", edad=28, ciudad="Madrid")

imprimir_detalles(producto="PC_ROG", precio=2999.99, stock=True)

imprimir_detalles(curso="Python", nivel="Intermedio", duracion="4 semanas")
