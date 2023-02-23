# importar librerias
import pandas as pd
import csv
import re
import requests
from bs4 import BeautifulSoup
import time
import random
import datetime

####Carga de CSV
nombre_de_csv = "yelpbatch1406to2302se.csv"
myheaders = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"]


def obtain_csv(file_name):
    doc = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            # print(line)
            doc.append(line)
    return doc


doc = obtain_csv(nombre_de_csv)
batch_doc = doc[10:800]


def busqueda_web(query, myheaders):
    headers = {
        "user-agent": myheaders[random.randint(0, 4)]
    }
    print(headers)
    # query = "RNR Tire Express B&B Rentals - Raytown 8910 E 350 Highway Raytown, MO 64133 yelp"
    url = "https://google.com/search?q=" + query.replace(" ", "+") + "&hl=en"
    respuesta = requests.get(url, headers=headers)
    print(respuesta.status_code)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    containers = soup.find_all("div", class_="g")
    return containers


def buscar_links(containers):
    probables_ligas = []
    for i in containers:
        # print(i.find("a",href=True)['href'])
        probables_ligas.append(str(i.find("a", href=True)['href']))
    return probables_ligas


def agregar_links(probables_ligas, batch_doc, n):
    for i in probables_ligas:
        if "yelp.com/biz" in i:
            batch_doc[n].append(i)
        else:
            pass


total = 0.0
for n in range(len(batch_doc)):
    # n=6
    # print("este es el query:")
    query = batch_doc[n][2]
    print(query)
    # print("este es el entry 0, comparar con final")
    print(batch_doc[n])
    try:
        containers = busqueda_web(query, myheaders)
        probables_ligas = buscar_links(containers)

        print(probables_ligas)
        agregar_links(probables_ligas, batch_doc, n)

        print(batch_doc[n])

        mimido = round(random.uniform(29, 61), 2)
        time.sleep(mimido)
        print("tiempo mimido")
        print(mimido)
        total = total + mimido
    except:
        mimido = round(random.uniform(29, 61), 2)
        time.sleep(mimido)
        print("tiempo mimido")
        print(mimido)
        total = total + mimido

df = pd.DataFrame(batch_doc)
df.to_csv('search_batch4_10_800.csv', index=False, header=False)
print("programa completado en:")
print(datetime.timedelta(seconds=total))
