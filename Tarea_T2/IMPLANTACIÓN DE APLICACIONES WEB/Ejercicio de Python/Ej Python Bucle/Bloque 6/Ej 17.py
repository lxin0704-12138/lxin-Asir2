import time
import random

print("Generando num aleatorios (hasta que salga > 8):")

while True:
    num_aleatorio = random.randint(1, 10)
    print(f"Numero generado: {num_aleatorio}")
    if num_aleatorio > 8:
        break
    time.sleep(0.5)

    