# Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero 
# positivo dado por el usuario.
numero = int(input("Ingrese un número entero positivo: "))
while numero < 0:
    print("Por favor, ingrese un número entero positivo.")
    numero = int(input("Ingrese un número entero positivo: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):              
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    