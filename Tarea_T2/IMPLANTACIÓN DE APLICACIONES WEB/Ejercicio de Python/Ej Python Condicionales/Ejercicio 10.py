precio = float(input("Ingresa el precio del producto: "))

if precio > 1000:
    descuento = precio * 0.1
    precio_final = precio - descuento
    print(f"Precio final con 10% de descuento: {precio_final:.2f}€")
else:
    print(f"Precio sin descuento: {precio:.2f}€")