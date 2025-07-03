# Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números 
# naturales: 1^2 + 2^2 + 3^2 +… + n^2.
n = int(input("Ingrese un número natural: "))
acumulador = 0
# Usando un ciclo for
# for i in range(1, n + 1):
#     cuadrado = i ** 2
#     print(cuadrado, end=" ")
#     acumulador += cuadrado
# print("\nLa suma de los cuadrados de los primeros", n, "números naturales es:", acumulador)
#Usando el ciclo while
i = 1
while i <= n:
    cuadrado = i ** 2
    print(cuadrado, end=" ")
    acumulador += cuadrado
    i += 1
print("\nLa suma de los cuadrados de los primeros", n, "números naturales es:", acumulador)