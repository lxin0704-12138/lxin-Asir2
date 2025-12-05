productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
suma_precios = 0

for precio in productos.values():
    suma_precios += precio

for producto, precio in productos.items():
    
    print(f"Producto: {producto}, Precio: {precio}€")
    
print(f"Precio total: {suma_precios:.2f}€")