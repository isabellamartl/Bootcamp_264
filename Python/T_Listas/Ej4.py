#Calcular la suma de todos los elementos de una lista en sus posiciones impares. 
lista = []
n=int(input("Ingrese cuantos números desea ingresar: "))
suma = 0
for i in range (1,n+1):
    num = int(input("Ingrese un número:"))
    lista.append(num)  # .append para agregar elementos a la lista
    if i % 2 != 0:  # Verifica si la posición es impar
        suma += num
print(f"La suma de los elementos {lista} en posiciones impares es: {suma}")
