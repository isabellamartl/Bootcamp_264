#Buscar en una lista de elementos numéricos, los elementos mayores a un valor X 
# dado por el usuario y mostrar cuantos se encontraron.
lista = []
mayores = []
n=int(input("Ingrese cuantos números desea ingresar: "))
x=int(input("Ingrese un número para evaluar los elementos mayores: "))
for i in range (1,n+1):
    num = int(input("Ingrese un número:"))
    lista.append(num) #.append para agregar elementos a la lista
for num in lista:
    if num > x:
        mayores.append(num)
        
print(f"Se encontraron {len(mayores)} y los números mayores que {x} son: {mayores}")

        