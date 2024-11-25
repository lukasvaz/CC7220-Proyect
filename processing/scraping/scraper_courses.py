import requests
from bs4 import BeautifulSoup
import csv
import os

# URL to scrape
url = 'https://ucampus.uchile.cl/m/fcfm_catalogo/?semestre=20242&depto=5' # set to  5 to DCC , set to 21 to DIM 

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
ramos=soup.find_all('div', class_="ramo")
existing_codigos=[]
if os.path.isfile('courses_info.csv'):
    with open('courses_info.csv', mode='r') as file:
        reader = csv.reader(file)
        # reader.__next__()
        existing_codigos= []
        for row in reader:
            existing_codigos.append(row[1])
else:
    with open('courses_info.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Titulo', 'Codigo', 'Creditos', 'Requisitos', 'Profesores', 'Departamento'])

with open('courses_info.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    for ramo in ramos:
            titulo=ramo.find('div' ,class_="objeto").find("h1").text.strip()
            codigo=ramo.find('div' ,class_="objeto").find("h2").text.strip()
            try:
                creditos=ramo.find_all('dd')[1].text
                requisitos=ramo.find_all('dd')[2].text.split(",")
            except:
                creditos=""
                requisitos=""
            
            secciones=ramo.find_all('ul', class_="profes")
            profes=[]
            for seccion in secciones:
                profes+=[profe.text.strip() for profe in  seccion.find_all('h1')]
            profes=list(set(profes))
            
            if codigo.startswith("CC"):
                departamento="DCC"
            else:
                departamento="DIM"
            
            if codigo not in existing_codigos:
                writer.writerow([titulo, codigo, creditos, requisitos, profes, departamento])