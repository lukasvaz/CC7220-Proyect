from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import requests
import csv
import sys
from dim import URLS as DIM_URLS
from dcc import URLS as DCC_URLS


# Set up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the Selenium WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

department={
    "DCC":["830",'Departamento de Ciencias de la Computación',DCC_URLS],
    "DIM":["828",'Departamento de Ingeniería Matemática',DIM_URLS]
}

# Read the input from stdin
if len(sys.argv) > 1:
    codigo = sys.argv[1]
else:
    print("Please provide the department code as a command-line argument.")
    sys.exit(1)

if codigo not in department:
    print(f"Invalid department code: {codigo}")
    sys.exit(1)

Selected = department[codigo]
URLS = Selected[2]

anchors = URLS
for a in anchors:
    driver.get(a)
    time.sleep(2) 
    prof_source = driver.page_source
    soup_response = BeautifulSoup(prof_source, 'html.parser')
    personal_info_div = soup_response.find('div', id='justify-tab-example-tabpane-informacion-personal').find('table')
    personal_info_list = []
    rows = personal_info_div.find_all('tr')
    for row in rows[1::]:
        cols = row.find_all('td')
        entry={"Grado": cols[0].text.strip(), "Institución": cols[1].text.strip(),"fecha":cols[2].text.strip()}  
        personal_info_list.append(entry)
    print(
        f""""
        Nombre: {soup_response.find('p',class_="AcademicProfile_academicTitle__no_Rn").text}
        Cargo: {soup_response.find_all('div',class_="AcademicProfile_nombramientoDetail__sTZwO")[0].text}
        Grados:{personal_info_list}
        Departamento: {Selected[1]},
        Código: {codigo}
        """
    )
    # Define the CSV file path
    csv_file_path = '/home/lukas/Escritorio/Proyecto-Watos/professors_info2.csv'

    # Define the CSV headers
    csv_headers = ['Nombre', 'Cargo', 'Grados', 'Departamento', 'Código']

    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        
        # Write the header only if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        # Write the professor's information to the CSV file
        writer.writerow({
            'Nombre': soup_response.find('p', class_="AcademicProfile_academicTitle__no_Rn").text,
            'Cargo': soup_response.find_all('div', class_="AcademicProfile_nombramientoDetail__sTZwO")[0].text,
            'Grados': personal_info_list,
            'Departamento': Selected[1],
            'Código': codigo
        })
driver.quit()














# Close the WebDriver
# url = root +'/unidad/788/departamento/'+Selected[0]  
# driver.get(url)
# anchors=[]
# # Wait for the page to load
# while True:
#     time.sleep(2)  # Adjust the sleep time as needed
#     page_source = driver.page_source
#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(page_source, 'html.parser')
#     divs = soup.find_all('div', class_="AcademicCard_nombre__MQcFY")
#     new_anchors = [div.find('a').get('href') for div in divs]
#     anchors += new_anchors 

#     # Find the button element by its class name or any other attribute
#     if len(new_anchors)<12:
#         break
    
#     button = driver.find_elements(By.CLASS_NAME, "PaginationServer_chevron__bmKZ7")[-1]
#     print(button.text)
#     if button:
#         # Scroll the button into view using JavaScript
#         driver.execute_script("arguments[0].scrollIntoView(true);", button)
#         time.sleep(5)  # Wait for the scrolling to complete
#         # driver.execute_script("arguments[0].click();", button)
#         button.click()
#         time.sleep(2)  

#     # button[-1].click()
#     time.sleep(2) 
#     break

# keep = True