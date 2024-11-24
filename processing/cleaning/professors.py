import csv

def extract_first_last_name(full_name):
    names = full_name.split()
    try:
        last_name = names[2]
    except IndexError:
        last_name = names[1]

    first_name = names[0]
    return first_name,last_name


input_file =  './outputs/scrapping/professors_info.csv'
output_file = './outputs/processing/professor_info_cleaned.csv'
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for i,row in enumerate(reader):
        if i == 0:
            continue
        full_name = row[0]
        first_name,last_name= extract_first_last_name(full_name)
        print(f"{first_name}  {last_name}")
        # row[0] = f"{first_name} {last_name}"
        # writer.writerow(row)