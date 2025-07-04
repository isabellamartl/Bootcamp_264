# Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos 
# negativos y cuantos son cero. 
num = int(input("Ingrese la cantidad de números que desea ingresar: "))
lista = []
for i in range(num):
    n = int(input("Ingrese un número: "))
    lista.append(n) 
positivos = 0
negativos = 0
ceros = 0
for n in lista:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")
print(f"Lista de números: {lista}")
