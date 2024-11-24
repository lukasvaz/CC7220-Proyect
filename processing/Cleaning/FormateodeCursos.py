
import csv
import re

#Este codigo formatea las mayoria de los nombres de los profesores pero existen algunas excepciones que tuvimos que arreglar a mano como es el caso
#Del curso de trabajo de titulo que al ser tantos profesores el scrapping lo formateo mal y tuvimos que arreglar el formateo a mano 
def procesar_profesores(profesores_str):
    if not profesores_str or profesores_str == "['No tiene']":
        return profesores_str
    
    # Extraer lista de nombres desde el string
    profesores = re.findall(r"'(.*?)'", profesores_str)
    profesores_formateados = []
    
    for profesor in profesores:
        # Dividir en palabras y filtrar las iniciales con punto
        palabras = profesor.split()
        palabras_validas = [palabra for palabra in palabras if not re.match(r'^[A-Z]\.$', palabra)]
        
        # Tomar las primeras dos palabras válidas
        if len(palabras_validas) >= 2:
            #Caso especial para formateo de un nombre de una profesora
            if palabras_validas[0] == "Sandra":
                nombre = palabras_validas[0]
                apellido = palabras_validas[3]
                profesores_formateados.append(f"{nombre}_{apellido}")
            else:    
                nombre = palabras_validas[0]
                apellido = palabras_validas[1]
                profesores_formateados.append(f"{nombre}_{apellido}")
    
    # Convertir la lista de nuevo a string con el formato adecuado
    return f"['{', '.join(profesores_formateados)}']"

def procesar_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Leer y escribir la cabecera sin modificar
        cabecera = next(reader)
        writer.writerow(cabecera)
        
        # Procesar las filas restantes
        for row in reader:
            if len(row) > 4:  # Asegurarse de que la columna de profesores exista
                row[4] = procesar_profesores(row[4])
            writer.writerow(row)

# Rutas de los archivos
archivo_entrada = 'cursos.csv'
archivo_salida = 'cursos_formateados.csv'

procesar_csv(archivo_entrada, archivo_salida)