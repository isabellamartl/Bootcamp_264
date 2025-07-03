# Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10, 
# dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales) 
numero_secreto = 7  # Número preestablecido
intentos = 3  # Número de intentos permitidos
while intentos > 0:
    adivina = int(input(f"Adivina el número (entre 1 y 10). Te quedan {intentos} intentos: "))
    if adivina == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break # Para salir del ciclo si se cumple
    else:
        intentos -= 1 # Disminuye el número de intentos
        if intentos > 0:
            print("Incorrecto. Inténtalo de nuevo.")
        else:
            print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")