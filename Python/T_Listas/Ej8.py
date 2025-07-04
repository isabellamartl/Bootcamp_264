# Buscar en una lista de elementos numéricos los elementos menores a un valor X dado 
# por el usuario y mostrar las posiciones donde están ubicados.
lista = []      
n = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(n):
    num = int(input("Ingrese un número: "))
    lista.append(num)           
x = int(input("Ingrese el valor X: "))
posiciones = [i for i, valor in enumerate(lista) if valor < x]

if posiciones:
    print(f"Los números menores a {x} se encuentran en las posiciones: {posiciones}")
else:
    print(f"No hay números menores a {x} en la lista.")
print(f"Lista de números: {lista}")