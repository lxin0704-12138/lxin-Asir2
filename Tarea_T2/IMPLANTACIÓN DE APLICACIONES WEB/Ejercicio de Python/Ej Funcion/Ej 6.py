def promedio(*args):
    if len(args) == 0:
        print("Error: No se proporcionaron números.")
        return 0
    return sum(args) / len(args)

print("Promedio de (2,4,6) =", promedio(2, 4, 6))
print("Promedio de (1,3,5,7,9) =", promedio(1, 3, 5, 7, 9))
print("Promedio de (1.5,4,2) =", promedio(1.5,4,2))
print("Promedio de (10) =", promedio(10))
print("Promedio sin números =", promedio())