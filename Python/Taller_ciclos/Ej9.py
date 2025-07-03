# Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio, 
# hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales). 
suma = 0
contador = 0
numero = float(input("Ingrese un número positivo (0 o negativo para salir): "))
# Mientras el número sea positivo,suma
while numero > 0:
    suma += numero
    contador += 1
    if contador > 0:
        promedio = suma / contador
    print(f"\nLa suma es: {suma}")
    print(f"El promedio es: {promedio:.2f}")
    numero = float(input("Ingrese otro número positivo (0 o negativo para salir): "))
