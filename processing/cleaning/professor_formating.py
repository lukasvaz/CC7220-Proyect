import csv
import ast
import datetime

def process_string(s):
    return s.replace('.', '').replace("'",'').replace('-', '').replace('/a','').replace('  ','_').replace(' ', '_').replace('""','"')

input_file = 'profesores_formateados.csv'
output_file = 'professor_formating_processed.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        row['Cargo'] = process_string(row['Cargo'])
        grados = ast.literal_eval(row['Grados'])
        for grado in grados:
            grado['Grado'] = process_string(grado['Grado'])
            grado['Institucion'] = process_string(grado['Institucion']).upper()
            grado['fecha']=datetime.datetime.strptime(grado['fecha'], '%d-%m-%Y').strftime('%Y-%m-%d')
        row['Grados'] = str(grados)
        writer.writerow(row)