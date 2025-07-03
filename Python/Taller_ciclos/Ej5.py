# Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de 
# temperaturas dadas por el usuario. 
temperaturas = []
for i in range(5):
    temp = float(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(temp)   
promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio de las temperaturas ingresadas es: {promedio:.2f} °C")
