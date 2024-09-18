import csv
import pandas as pd

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

encabezadosInicial=['cantidad','Referencia','ReferenciaCopy','codigo','Compuesto','Uso','Aplicacion','Marca','vacio','vacioCopy','vacioCopyCopy']

# Escribir en el archivo CSV
with open("datoInicial.csv", mode="w", newline="") as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(encabezadosInicial)
    escritor_csv.writerows([line.split(',') for line in dato_Doble_punto_y_Coma])

############################################
###### paso 3: tratamos cada columna #######
############################################

data = pd.read_csv('datoInicial.csv', header=0, skipinitialspace=True, encoding='utf-8')

data.drop('vacio', axis=1, inplace=True)
data.drop('vacioCopy', axis=1, inplace=True)
data.drop('vacioCopyCopy', axis=1, inplace=True)

# Agregar una nueva columna 'Producto' con lo mismo de cantidad
data['Producto'] = data['cantidad']

# Eliminar todos los espacios en blanco
data['cantidad'] = data['cantidad'].str.replace(r'\s+', '', regex=True)

# Eliminar todo a partir de la primera 'U' en las columnas 'cantidad' y 'Producto'
data['cantidad'] = data['cantidad'].str.replace(r'U.*', '', regex=True)

# Eliminar todo antes de la 'K', incluyendo la 'K'
data['Producto'] = data['Producto'].str.replace(r'^.*K', 'K', regex=True)

# Escribir el archivo CSV con el encabezado actualizado
data.to_csv('datoEnTrasformacion.csv', index=False)

###################
#####
######

encabezadosFinal=['Unidades','Productos','Referencia','codigo','Compuesto','Uso','Aplicacion','Marca']