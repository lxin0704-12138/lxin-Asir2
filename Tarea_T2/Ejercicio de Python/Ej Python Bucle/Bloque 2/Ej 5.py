productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
suma_precios = 0

for precio in productos.values():
    suma_precios += precio

print(f"Suma total de precios: {suma_precios:.2f}€")