#  Calcular y visualizar la suma y el producto de los números pares comprendidos entre 
# 20 y 400 ambos inclusive. 
n = 20
m = 400
acumulador_suma = 0
acumulador_producto = 1
# Usando un ciclo for
for i in range(n, m + 1):
    if i % 2 == 0:  # Verifica si el número es par
        acumulador_suma += i
        acumulador_producto *= i
# print(f"La suma de los números pares entre {n} y {m} es: {acumulador_suma}")
# print(f"El producto de los números pares entre {n} y {m} es: {acumulador_producto}")
