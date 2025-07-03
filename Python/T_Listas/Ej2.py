# Calcular la suma de todos los elementos de una lista de n posiciones. 
lista = []
n=int(input("Ingrese cuantos números desea ingresar: "))
suma = 0
for i in range (1,n+1):
    num = int(input("Ingrese un número:"))
    lista.append(num) #.append para agregar elementos a la lista
    suma += num
print(suma)
 
