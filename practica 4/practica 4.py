#Graficando
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv(r'C:\Users\Joséluis\Documents\Python_practicas\Characters_GF_V1.3.csv')

a = datos['Health_Points']
b = datos['Damage']
c = datos['ACC']
d = datos['Evasion']
e = datos['R_o_F']
f = datos['Year_Prod']

x = datos['Index_Tdoll']

types_counts = datos.groupby('Gun-Type')['Name_T-doll'].count()

roles_counts = datos.groupby('Role_T-doll')['Name_T-doll'].count()

country_counts = datos.groupby('Country_origin')['Name_T-doll'].count()

year_counts = datos.groupby('Year_Prod')['Name_T-doll'].count()


plt.scatter(x, a)
plt.xlabel("Index Tdolls", fontsize=20)
plt.ylabel("HP points", fontsize=20)
plt.savefig("dollXhp.png") #Grafica de HP x dolls
plt.close()

plt.scatter(x, b)
plt.xlabel("Index Tdolls", fontsize=20)
plt.ylabel("DMG points", fontsize=20)
plt.savefig("dollXdamage.png") #Grafica de DMG x dolls
plt.close()

plt.scatter(x, c)
plt.xlabel("Index Tdolls", fontsize=20)
plt.ylabel("ACC points", fontsize=20)
plt.savefig("dollXacc.png") #Grafica de ACC x dolls
plt.close()

plt.scatter(x, d)
plt.xlabel("Index Tdolls", fontsize=20)
plt.ylabel("EVA points", fontsize=20)
plt.savefig("dollXeva.png") #Grafica de EVA x dolls
plt.close()

plt.scatter(x, e)
plt.xlabel("Index Tdolls", fontsize=20)
plt.ylabel("RoF points", fontsize=20)
plt.savefig("dollXrof.png") #Grafica de RoF x dolls
plt.close()

types_counts.plot(kind='bar',title="Cantidad de Tdolls por Tipo de Arma")
plt.savefig("Type_count.png") #Grafica de RoF x dolls
plt.close()

roles_counts.plot(kind='bar',title="Cantidad de Tdolls por Rol en Combate")
plt.savefig("Role_count.png") #Grafica de RoF x dolls
plt.close()

country_counts.plot(kind='line',title="Cantidad de Tdolls por Pais de Origen")
plt.savefig("Country_count.png") #Grafica de RoF x dolls
plt.close()

year_counts.plot(kind='line',title="Cantidad de Tdolls por Año de Producción")
plt.savefig("Date_count.png") #Grafica de RoF x dolls
plt.close()