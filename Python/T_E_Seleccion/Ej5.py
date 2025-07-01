#Calcular la nómina semanal (salario neto) de un trabajador de una empresa cuyo trabajo se paga por horas. Leer por teclado el número de horas y el precio de la hora. 
#El cálculo se realiza del siguiente modo: 
#• Las primeras 35 horas se pagan a la tarifa normal. 
#• Las horas extras se pagan un 25% más que las normales. 
#• Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual. 
#• Si el sueldo es menor de 1000€, libre de impuestos. 
#• Si el sueldo está entre 1000€ y 2000€, los impuestos son el 20%. 
#• Si el sueldo es mayor de 2000€, el 30%.
horas = int(input("Ingrese el número de horas :"))
precio = float(input("Ingrese el precio de la hora :"))
if horas <= 35 :
    salario_bruto = precio * horas
    print (salario_bruto) 
else:
    horas_extra = horas - 35
    salario_bruto = (precio*35)+ (horas_extra * precio * 1.25)
    print (salario_bruto)
salario_mensual = salario_bruto*4
print (f" salario mensual:{salario_mensual}")
if salario_mensual <1000 :
    salario_neto = salario_mensual
    print (f"Su salario está libre de impuestos {salario_neto}")
elif salario_mensual >= 1000 and salario_mensual <= 2000 :
    salario_neto = (salario_mensual)- (salario_mensual*0.20)
    print (f"Su salario es con un impuesto del 20% : {salario_neto}")
else:
    salario_neto = (salario_mensual) - (salario_mensual*0.30)
    print (f"Su salario es con un impuesto del 30%: {salario_neto}")

