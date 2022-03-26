#Limpieza de datos
import pandas as pd

df1=pd.read_csv(r"C:\Users\Joséluis\Documents\Python_practicas\Personajes_GirlsFrontline.csv") 
#Es donde se hizo mi .csv ^^;; 

#LLENANDO TODOS LOS VALORES NAN

#Columna Rol de T-doll
df1['Rol_de_T-doll'] = df1['Rol_de_T-doll'].fillna("Versatile") 
#Columna Tiempo de Producción / tiempo promedio en hacer login u Dropeo en mapas
df1['Tiempo_de_Produccion'] = df1['Tiempo_de_Produccion'].fillna("00:05:00")
#Columna Obtención
df1['Obtencion'] = df1['Obtencion'].fillna("Unknown")

for i in df1['Obtencion']:
    dato = str(i)
    datoC = dato.find("\n")
    if datoC != -1:
        datoM = dato[10:]
        df1['Obtencion'] = df1['Obtencion'].replace([dato], datoM)

#Redundancia en los roles por una coma
df1.loc[df1['Rol_de_T-doll'] == '"Burst,"','Rol_de_Tdoll']='Burst'
df1.loc[df1['Rol_de_T-doll'] == '"Burst, Sustained,"','Rol_de_Tdoll']='Burst, Sustained'
df1.loc[df1['Rol_de_T-doll'] == '"Main Tank,"','Rol_de_Tdoll']='Main Tank'
df1.loc[df1['Rol_de_T-doll'] == '"Night,"','Rol_de_Tdoll']='Night'
df1.loc[df1['Rol_de_T-doll'] == '"Night, Burst,"','Rol_de_Tdoll']='Night, Burst'
df1.loc[df1['Rol_de_T-doll'] == '"Specialist,"','Rol_de_Tdoll']='Specialist'
df1.loc[df1['Rol_de_T-doll'] == '"Sustained,"','Rol_de_Tdoll']='Sustained'

#Casos Unicos
df1.loc[df1['Nombre_de_T-doll'] == 'LTLX-7000','Obtencion']='Normal'
df1.loc[df1['Nombre_de_T-doll'] == 'Kar98K','Obtencion']='Heavy, Normal'
df1.loc[df1['Nombre_de_T-doll'] == 'SPAS-12','Obtencion']='Heavy'
df1.loc[df1['Nombre_de_T-doll'] == 'Type 79','Obtencion']='Heavy, Normal'
df1.loc[df1['Nombre_de_T-doll'] == 'P99','Obtencion']='Normal'
df1.loc[df1['Nombre_de_T-doll'] == 'IWS-2000','Obtencion']='Heavy, Normal'
df1.loc[df1['Nombre_de_T-doll'] == 'USP Compact','Obtencion']='Normal'

df1.to_csv('P_GF_limpio.csv')
