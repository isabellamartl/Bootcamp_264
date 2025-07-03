# Escribir un algoritmo que calcule la suma de los n primeros números naturales. 
# Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por el usuario.
# += Es una asignación compuesta, equivale a acumulador = acumulador + i
n = int(input("Ingrese un número natural: "))
acumulador = 0 
# Usando un ciclo for
# n + 1 para incluirlo en el rango
# for i in range (1,n + 1,1):
#      print(i, end=" ")
#      acumulador += i
# print("\nLa suma de los primeros", n, "números naturales es:", acumulador)
# Usando un ciclo while
i = 1       
while i <= n:
    print(i, end=" ")
    acumulador += i
    i += 1
print("La suma de los primeros", n, "números naturales es:", acumulador)