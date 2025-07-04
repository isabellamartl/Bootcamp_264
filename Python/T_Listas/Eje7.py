#Determinar si un número X dado por el usuario se encuentra repetido o no en una lista 
#de elementos numéricos. 
lista = []
n = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(n):
    num = int(input("Ingrese un número: "))
    lista.append(num)
x = int(input("Ingrese el número X a buscar: "))
if x in lista:
    print(f"El número {x} se encuentra en la lista.")
else:
    print(f"El número {x} no se encuentra en la lista.")
print(f"Lista de números: {lista}")
# Verificar si el número X se repite    
repeticiones = lista.count(x)
if repeticiones > 1:
    print(f"El número {x} se repite {repeticiones} veces en la lista.")
else:
    print(f"El número {x} no se repite en la lista.")
# Verificar si el número X es único
if repeticiones == 1:
    print(f"El número {x} es único en la lista.")
else:
    print(f"El número {x} no es único en la lista.")
