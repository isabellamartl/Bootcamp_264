# Calcular los cuadrados de todos los elementos de una lista.
lista = []
lista_cuadrado = []
n=int(input("Ingrese cuantos números desea ingresar: "))


for i in range (1,n+1):
    num = int(input("Ingrese un número:"))
    lista.append(num) #.append para agregar elementos a la lista
    cuadrado = num**2
    lista_cuadrado.append(cuadrado)

print(f"los cuadrados de {lista} son {lista_cuadrado}")

