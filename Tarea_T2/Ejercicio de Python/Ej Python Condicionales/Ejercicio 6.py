letra = input("Ingresa una letra: ").lower()  # .lower() 转为小写，兼容大写输入

vocales = ["a", "e", "i", "o", "u"]
if letra in vocales:
    print("Es una vocal.")
else:
    print("No es una vocal.")