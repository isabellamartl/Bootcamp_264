# Implementar un algoritmo que calcule el producto de dos números enteros (n*m) 
# haciendo sólo sumas.
n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))
# Acumulador para el producto
producto = 0
# Usando un ciclo for
for i in range(m):
    producto += n       
print(f"El producto de {n} x {m} es: {producto}")
# Usando un ciclo while
# i = 0           
# while i < m:
#     producto += n
#     i += 1
# print(f"El producto de {n} x {m} es: {producto}")


