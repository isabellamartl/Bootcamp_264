import numpy as np
import matplotlib.pyplot as plt
edades = [38,25,42,18,32,16,22,43,39,27]
suma = np.sum(edades)
print("suma:", suma)

datos = np.count_nonzero(edades)#nos permite contar todos los elementos != de 0
print("cantidad:",datos)

prom = np.mean(edades)
print("promedio:", prom)

mediana = np.median(edades)
print("Mediana:", mediana)

minimo = np.min(edades)
print("minimo :", minimo)

maximo =np.max(edades)
print("maximo:" , maximo)

desviacion = np.std(edades)
print("desviacion:" , desviacion)

x= np.linspace(1,10,10)# puntos a graficar
y = np.array(edades)

plt.plot(x,y, color= 'green', linestyle='-', marker ='o')
plt.title("Gráfico matplotlib")
plt.grid()
plt.show()
