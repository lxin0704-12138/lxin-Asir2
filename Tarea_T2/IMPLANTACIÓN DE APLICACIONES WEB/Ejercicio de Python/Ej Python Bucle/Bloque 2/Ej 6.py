productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
umbral = 1.0
productos_caros = []

for producto, precio in productos.items():
    if precio > umbral:
        productos_caros.append(producto)

print(f"Productos con precio > {umbral}€: {productos_caros}")