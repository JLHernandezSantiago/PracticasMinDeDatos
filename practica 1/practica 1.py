#Obteniendo datos por WEBscraping // tal vez debí escoger otra webpage, pero lo queria intentar
#Duda, como obtener los datos que estan en un <li [datos]></li> ????

import requests
from bs4 import BeautifulSoup
import pandas as pd

# indicar la ruta
URL = 'https://blitzhangar.com/'

# Realizamos la petición a la web
req = requests.get(URL)

# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
soup = BeautifulSoup(req.text, "lxml")

# Obtenemos todos los divs donde están las entradas
entradas1 = soup.find_all('a', {'class': 'tank-name-link tank-quality--researchable'}) 
entradas2 = soup.find_all('a', {'class': 'tank-name-link tank-quality--collectible'})
entradas3 = soup.find_all('a', {'class': 'tank-name-link tank-quality--premium'})

tanklist1 = [] #tanques investigables
tanktier1 = [] 

tanklist2 = [] #tanques de coleccion
tanktier2 = [] 

tanklist3 = [] #tanques premium
tanktier3 = [] 

for i in entradas1: 
    span1 = i.find('span', {'class': 'tank-name-link__name'})
    spanA = i.find('span', {'class': 'tank-name-link__tier'})
    tanklist1.append(span1.string)
    tanktier1.append(spanA.string)  
  
#print(tanklist1)

for j in entradas2: 
    span2 = j.find('span', {'class': 'tank-name-link__name'})
    spanB = j.find('span', {'class': 'tank-name-link__tier'})
    tanklist2.append(span2.string)
    tanktier2.append(spanB.string) 
  
#print(tanklist2)

for k in entradas3: 
    span3 = k.find('span', {'class': 'tank-name-link__name'})
    spanC = k.find('span', {'class': 'tank-name-link__tier'})
    tanklist3.append(span3.string)
    tanktier3.append(spanC.string) 
  
#print(tanklist3)

df = pd.DataFrame({"Tanques investigables": tanklist1, "Tier del tanque":tanktier1})   
df.to_csv('tanques invest.csv')

df = pd.DataFrame({"Tanques Premium": tanklist3, "Tier del tanque":tanktier3})   
df.to_csv('tanques premium.csv')

df = pd.DataFrame({"Tanques De Coleccion": tanklist2, "Tier del tanque":tanktier2})   
df.to_csv('tanques collection.csv')
