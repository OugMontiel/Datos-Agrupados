import csv
import re

with open('dato.txt', 'r') as file:
    dato = file.read()

######################################## 
###### Paso 1 : Estructurar datos ######
########################################

dato_Doble_punto_y_Coma = dato.split(';;')
with open('dato_Doble_punto_y_Coma.txt', 'w') as file:
    file.write("\n".join(dato_Doble_punto_y_Coma))

dato_punto_y_coma = []
for producto in dato_Doble_punto_y_Coma:
    dato_punto_y_coma = producto.split(';')
    dato_punto_y_coma.extend(dato_punto_y_coma)
with open('dato_punto_y_coma.txt', 'w') as file:
    file.write("\n".join(dato_punto_y_coma))

dato_coma = []
for producto in dato_Doble_punto_y_Coma:
    dato_punto_y_coma = producto.split(',')
    dato_coma.extend(dato_punto_y_coma)
with open('dato_coma.txt', 'w') as file:
    file.write("\n".join(dato_coma))

############################################  
###### Paso 2: Procesar cada producto ######
############################################

estructura_productos = []
for producto in dato_coma:
    # Eliminar caracteres innecesarios como espacios en blanco adicionales
    producto = producto.strip()
    
    # Buscar patrones clave: cantidad, referencia, código y composición
    cantidad = re.search(r'\d+\.?\d*\s+UNIDAD', producto)
    referencia = re.search(r'REF=\s*([\w-]+)', producto)
    codigo = re.search(r'CODIGO\s*([\w-]+)', producto)
    compuesto = re.search(r'COMPUESTO\s*([\w\s=]+)', producto)
    uso = re.search(r'USO=\s*(\w+)', producto)
    marca = re.search(r'MARCA=\s*(\w+)', producto)
    
    # Agregar al resultado estructurado
    estructura_productos.append({
        "cantidad": cantidad.group() if cantidad else None,
        "referencia": referencia.group(1) if referencia else None,
        "codigo": codigo.group(1) if codigo else None,
        "compuesto": compuesto.group(1) if compuesto else None,
        "uso": uso.group(1) if uso else None,
        "marca": marca.group(1) if marca else None
    })

# Nombre del archivo CSV
archivo_csv = "cadena_distribucion.csv"

# Obtener los encabezados de los diccionarios (asumiendo que todas las claves son consistentes)
encabezados = estructura_productos[0].keys()

# Escribir los datos en el archivo CSV
with open(archivo_csv, mode="w", newline="") as archivo:
    escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
    
    # Escribir la fila de encabezados
    escritor_csv.writeheader()
    
    # Escribir las filas de datos
    escritor_csv.writerows(estructura_productos)

print(f"Archivo '{archivo_csv}' generado exitosamente.")