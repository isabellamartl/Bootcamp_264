# Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo 
# m>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el 
# usuario.
n = int(input("Ingrese un número: "))
m = int(input("Ingrese un número mayor: "))
acumulador = 0
# for i in range(n, m + 1):
#     print(i, end=" ")
#     acumulador += i  
# print("\nLa suma de los números enteros de", n, "a", m, "es:", acumulador)
# Usando un ciclo while
i = n
while i <= m:
    print(i, end=" ")
    acumulador += i  
    i += 1
print("\nLa suma de los números enteros de", n, "a", m, "es:", acumulador)
