#Open contiene el archivo que se va a abrir, si el archivo no se encuentra en la ruta, se crea
#"w" modificador para escribir (abre el archivo modo escritura)
archivo = open("mi_archivo.txt", "w")
#\n para ingresar un salto de línea
#.write para generar linea de texto
archivo.write("Esta es mi primera linea.\n")
archivo.write("Esta es mi segunda linea.\n")

for i in range (3):
    archivo.write(f"Esta es la linea {i+3}.\n")
archivo.close () #Cierra el archivo
#"r" modificador para leer el archivo (abre archivo modo lectura)
archivo= open ("mi_archivo.txt","r")
#Me permite leer el archivo
contenido = archivo.read()
print(contenido)

for linea in contenido.split('/n'):#Para ver el contenido linea por linea
    print(linea)

  
