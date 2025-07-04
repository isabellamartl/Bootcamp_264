#Determinar si un número X dado por el usuario se encuentra repetido o no en una lista 
#de elementos numéricos. 
lista = []
n = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(n):
    num = int(input("Ingrese un número: "))
    lista.append(num)
x = int(input("Ingrese el número X a buscar: "))
if lista.count(x) > 0:
    print(f"El número {x} se encuentra en la lista y se repite {lista.count(x)} veces.")
else:
    print(f"El número {x} no se encuentra en la lista.")
print(f"Lista de números: {lista}")
