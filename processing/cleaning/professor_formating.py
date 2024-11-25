import csv
import ast

def process_string(s):
    return s.replace('.', '').replace('-', '').replace('  ','_').replace(' ', '_').replace('""','"')

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
            grado['Institucion'] = process_string(grado['Institucion'])
        row['Grados'] = str(grados)
        writer.writerow(row)