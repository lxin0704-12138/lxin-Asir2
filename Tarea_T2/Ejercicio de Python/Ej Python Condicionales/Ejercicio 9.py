temperatura = float(input("Ingresa la temperatura en Celsius: "))

if temperatura >= 30:
    print("Hace calor.")
elif 10 <= temperatura <= 29:
    print("El clima es templado.")
else:
    print("Hace frío.")