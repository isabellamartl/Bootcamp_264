
import json #Importar librería
with open ('mi_archivo.json','r') as file: #Para abrir el archivo
    data = json.load(file) #Para cargar archivos
    print(data)

    my_data = [{'nombre':'Juan','edad':30,'valor':789},
               {'nombre':'Rose', 'edad':23, 'valor':910}
               ]
    with open('otro_archivo.json','w') as file:
        json.dump(my_data, file, indent=4) #my_data: tipo obejto(en este caso un arreglo-diccionario) , file= alias del archivo(si no existe, lo crea), indent=4(opcional, organiza el archivo)) 
    