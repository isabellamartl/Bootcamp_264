# #Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a 
# viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla.
horas_extras = []
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
tarifa = float(input("Ingrese la tarifa de pago por hora extra: ")) 
for i in range(5):
    horas = float(input(f"Ingrese las horas extras trabajadas el {dias[i]}: "))
    horas_extras.append(horas)
total_pago = sum(horas_extras) * tarifa
print(f"El valor total a pagar por las horas extras trabajadas es: ${total_pago:.2f}")
