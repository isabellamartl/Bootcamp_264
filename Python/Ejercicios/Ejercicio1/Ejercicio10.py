hora = int(input("Ingrese el número de horas trabajadas : "))
precio = int(input("Ingrese cuanto cobra por hora"))
salario = (hora * precio )
imp= salario*0.08 
salnto = salario - imp
print ( "Su salario neto es:", salnto)