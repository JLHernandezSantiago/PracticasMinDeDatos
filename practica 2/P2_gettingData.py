#Obteniendo datos por WEBscraping 
#Y depurar despues de obtener datos, pero antes de crear el csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

# indicar la ruta
URL = 'https://gamepress.gg/girlsfrontline/t-dolls-list'

# Realizamos la petición a la web
req = requests.get(URL)

# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
soup = BeautifulSoup(req.text, "lxml")

# Obtenemos todos los divs donde están las entradas
entradas = soup.find_all('tr', {'class': 't-doll-new-row'}) 

# Obtain information
TdollName = []
TdollType = []
TdollRole = []
TdollTimecraft = []
TdollTypeCraft = []
TdollHp = [] 
TdollDmg = [] 
TdollAcc = [] 
TdollEva = [] 
TdollRof = []

for i in entradas:
    dollName = i.find('div').getText()
    dollRole = i.find('td', {'colspan':'5'}).text.strip()
    dollType = i.find('td', {'class':'class-cell'}).text.strip()
    dollTC = i.get('data-timer').strip()
    dollTyC = i.find('td', {'class':'timer-cell'}, 'div').text.strip() #ocupa limpieza
    dollHp = i.get('data-hp') #health points
    dollDmg = i.get('data-dmg') #damage
    dollAcc = i.get('data-acc') #accuracy
    dollEva = i.get('data-eva') #evasion
    dollRof = i.get('data-rof') #rate of fire
    
    TdollName.append(dollName)
    TdollRole.append(dollRole)
    TdollType.append(dollType)
    TdollTimecraft.append(dollTC)
    TdollTypeCraft.append(dollTyC)

    TdollHp.append(dollHp)
    TdollDmg.append(dollDmg)
    TdollAcc.append(dollAcc)
    TdollEva.append(dollEva)
    TdollRof.append(dollRof)

df = pd.DataFrame({
    "Nombre_de_T-doll": TdollName, 
    "Tipo_de_Arma": TdollType,
    "Rol_de_T-doll": TdollRole,
    "Tiempo_de_Produccion": TdollTimecraft,
    "Obtencion": TdollTypeCraft,
    "Puntos_de_vida":TdollHp,
    "Daño":TdollDmg,
    "Precision":TdollAcc,
    "Evasion":TdollEva,
    "Cadencia_de_Disparo":TdollRof
    })
       
df.to_csv('Personajes_GirlsFrontline.csv')