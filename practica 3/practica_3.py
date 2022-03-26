#analisis de datos
import pandas as pd

my_df = pd.read_csv("practica 2/P_GF_limpio.csv")

del(my_df['Unnamed: 0.1']) #creado al abrirlo aqui
del(my_df['Unnamed: 0']) #creado en la practica 2 :/

TipoGun = pd.unique(my_df['Tipo_de_Arma']) 
print(TipoGun) #como imprimió, hay solo 6 tipos: HG, SMG, AR, RF, MG, SG

Duracion_crafteo = my_df['Tiempo_de_Produccion'].describe() 
print("\nDescribe() del tiempo de produccion\n",Duracion_crafteo) #mostró Count, Unique, Top y freq

HPDescribe = my_df['Puntos_de_vida'].describe() 
print("\nDescribe() de los Puntos de Vida\n",HPDescribe) #mostró Count, Unique, Top y freq

grouped_data = my_df.groupby('Tipo_de_Arma') #Agrupando por tipo de arma
print("\nDescribe() por tipo de arma\n", grouped_data.describe()) #describio las datos tipo float por tipo de arma, LOL
print("\nimprimiendo solo la Media de lo anterior\n", grouped_data.mean())

types_counts = my_df.groupby('Tipo_de_Arma')['Nombre_de_T-doll'].count() #contando el numero de tdolls de acuerdo 
print("\nContando tdolls x tipo", types_counts) #con el tipo de arma

types_countsE = my_df.groupby('Rol_de_T-doll')['Nombre_de_T-doll'].count()['Versatile'] #lo mismo, pero solo
print("\nContando tdolls con rol Versatile:", types_countsE) # los rol "Versatile"

gD = my_df.groupby('Rol_de_T-doll') #Agrupando por tipo de rol
print("\nPromedio de Stats por Rol de Tdoll\n", gD.mean()) #Promedio De stats por cada tipo de rol