#importar librerias
import pandas as pd
import csv
import re
import requests
from bs4 import BeautifulSoup
####Carga de CSV
nombre_de_csv="sample - Sheet1.csv"
def obtain_csv(file_name):
    doc=[]
    with open(file_name,'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            #print(line)
            doc.append(line)
    return doc


doc=obtain_csv(nombre_de_csv)
batch_doc=doc[0:30]
query=batch_doc[0][3]
print(query)
#print(batch_doc)


# frase_buscar=[]
# for x in doc:
#     frase_buscar.append(x[3])
#
# print(frase_buscar[0:30])
# print(len(frase_buscar))

####Web scrapping

def busqueda_web(query):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }
    query = "RNR Tire Express B&B Rentals - Raytown 8910 E 350 Highway Raytown, MO 64133 yelp"
    url = "https://google.com/search?q=" + query.replace(" ", "+") + "&hl=en"
    respuesta = requests.get(url, headers=headers)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    containers = soup.find_all("div", class_="g")
    return containers

containers=busqueda_web()
# headers ={
# 	"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
# }
# query = "RNR Tire Express B&B Rentals - Raytown 8910 E 350 Highway Raytown, MO 64133 yelp"
# url="https://google.com/search?q="+query.replace(" ", "+")+"&hl=en"
#
# respuesta = requests.get(url, headers=headers)
#
# soup = BeautifulSoup(respuesta.text, "html.parser")
# #print(soup.prettify())
# containers = soup.find_all("div", class_="g")
#print(containers)
#first_find = containers.find("div", data-header-feature="0")
#print(first_find)
print(len(containers))
test_doc=[]
bandera=0

def buscar_links(containers):
    probables_ligas=[]
    for i in containers:
        #print(i.find("a",href=True)['href'])
        probables_ligas.append(str(i.find("a",href=True)['href']))
    return probables_ligas

def agregar_links(probables_ligas,doc):
    for i in probables_ligas:
        if "yelp.com/biz" in i:
            doc[0].append(i)
        else:
            pass


containers=busqueda_web()
probables_ligas=buscar_links(containers)
print(probables_ligas)
print(doc[0])




####################################################

#print(containers[0].find("a")['href'])
##########
#containers[0]
#link=str(containers[0].find("a")['href'])
#print(link)
# if "yelp.com/biz" in link:
#     print("Si esta")
# else:
#     print("no esta")
# review=containers[0].find("g-review-stars").next_sibling.next_sibling
# print(type(review))

#############
# for i in containers:
#     print(i.find("h3").get_text())
#     print(i.find("a")['href'])

#print(type(containers))
#divs=soup.select("#search div.g")
#print(divs)
#for i in containers:
#   print(i)
# divs = soup.select("#search div.g")
# for div in divs:
#     # Search for a h3 tag
#     results = div.select("h3")
#     # Check if we have found a result
#     if (len(results) >= 1):
#         # Print the title
#         h3 = results[0]
#         print(h3.get_text())
