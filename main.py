import csv
import re

with open('dato.txt', 'r') as file:
    dato = file.read()

######################################## 
###### Paso 1 : Estructurar datos ######
########################################

dato_Doble_punto_y_Coma = dato.split(';;')
identificadores = dato_Doble_punto_y_Coma[0]  
del dato_Doble_punto_y_Coma[0]  # Elimina la primera línea (identificadores)
nota = dato_Doble_punto_y_Coma[-1]  
del dato_Doble_punto_y_Coma[-1]  # Elimina la última línea (nota)
with open('dato_Doble_punto_y_Coma.txt', 'w') as file:
    file.write("\n".join(dato_Doble_punto_y_Coma))

############################################  
###### Paso 2: generamos csv  ######
############################################

encabezadosInicial=['UnidadesYProducto','Referencia','ReferenciaCopy','codigo','Compuesto','Uso','Aplicacion','Marca','vacio','vacioCopy']

# Escribir en el archivo CSV
with open("datoInicial.csv", mode="w", newline="") as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(encabezadosInicial)
    escritor_csv.writerows([line.split(',') for line in dato_Doble_punto_y_Coma])

############################################
###### paso 3: tratamos cada columna #######
############################################

with open('datoInicial.csv', mode='r') as file:
    lines = file.readlines()



encabezadosFinal=['Unidades','Productos','Referencia','codigo','Compuesto','Uso','Aplicacion','Marca']