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
# Eliminar todo antes de la 'K', incluyendo la 'K'
data['Producto'] = data['Producto'].str.replace(r'^.*K', 'K', regex=True)
# Limpiar la columna 'Producto'
data['Producto'] = data['Producto'].str.replace(r'\s+', ' ', regex=True).str.strip()


# Eliminar todos los espacios en blanco
data['cantidad'] = data['cantidad'].str.replace(r'\s+', '', regex=True)
# Eliminar todo a partir de la primera 'U' en las columnas 'cantidad' y 'Producto'
data['cantidad'] = data['cantidad'].str.replace(r'U.*', '', regex=True)
# Convertir 'cantidad' a tipo numérico (convertir de texto a float)
data['cantidad'] = pd.to_numeric(data['cantidad'])
# Si deseas convertir a entero después de convertir a float (opcional)
data['cantidad'] = data['cantidad'].astype('Int64')

# Eliminar 'REF=' de la columna 'descripcion'
data['Referencia'] = data['Referencia'].str.replace('REF=', '', regex=False)
# Unir 'referencia' y 'referencia_copy' en una nueva columna 'referencia_unida'
data['Referencia'] = data['Referencia'] + ' / ' + data['ReferenciaCopy']
# Eliminar todos los espacios en blanco
data['Referencia'] = data['Referencia'].str.replace(r'\s+', '', regex=True)
data.drop('ReferenciaCopy', axis=1, inplace=True)

# Eliminar 'CODIGO ' de la columna 'codigo'
data['codigo'] = data['codigo'].str.replace('CODIGO', '', regex=False)
# Eliminar todos los espacios en blanco
data['codigo'] = data['codigo'].str.replace(r'\s+', '', regex=True)

# Eliminar 'COMPUESTO ' de la columna 'Compuesto'
data['Compuesto'] = data['Compuesto'].str.replace('COMPUESTO ', '', regex=False)

# Eliminar 'USO=  ' de la columna 'Uso'
data['Uso'] = data['Uso'].str.replace('USO=', '', regex=False)
# Eliminar todos los espacios en blanco
data['Uso'] = data['Uso'].str.replace(r'\s+', '', regex=True)

# Eliminar 'MARCA= ' de la columna 'Marca'
data['Marca'] = data['Marca'].str.replace('MARCA=', '', regex=False)
# Eliminar todos los espacios en blanco
data['Marca'] = data['Marca'].str.replace(r'\s+', '', regex=True)

# Eliminar 'EN MOTORES DE VEHICULOS' de la columna 'Aplicacion
data['Aplicacion'] = data['Aplicacion'].str.replace('EN MOTORES DE VEHICULOS', '', regex=False)

########################################################################
###### paso 4: Renombramos las columna y generamos archivo final #######
########################################################################
# Reordenar columnas
encabezadosFinal=['cantidad','Producto','Referencia','codigo','Compuesto','Uso','Aplicacion','Marca']
data = data[encabezadosFinal]

# Escribir el archivo CSV con el encabezado actualizado
data.to_csv('datoFinal.csv', index=False)