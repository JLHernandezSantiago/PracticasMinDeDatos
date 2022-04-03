#Realizando pruebas de hipotesis, Es un codigo avestruz dado a que no me deja correrlo mi lap
#Porque no se importa correctamente el "scipy", pero tecnicamente debe funcionar sin problemas
from scipy import stats
import numpy as np
import pandas as pd

datos = pd.read_csv('././Documents/Python_practicas/Characters_GF_V1.3.csv')

example1 = datos['Health_Points']
exa1mean = datos['Health_Points'].mean() #140.3132
exa1std = datos['Health_Points'].std() #74.2049

#INTERVALOS DE CONFIANZA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mean = 142
std = 77

se = exa1std/np.sqrt(len(example1))

min_ = exa1mean - 2 * se
max_ = exa1mean + 2 * se
print("Intervalo de confianza (confianza del 95%):", (min_, max_))

#PRUEBA Z ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
se2 = std / np.sqrt(len(example1))

# Estadísticas Z
Z2 = (exa1mean - mean) / se2

print("La estadística Z es {}".format(Z2))

# Valor P
P2 = 2 * stats.norm.sf(abs(Z2)) 
# Aquí stats.norm.sf () devuelve el área en el lado derecho de Z, por lo que * 2 es 
# la suma de las áreas en los lados izquierdo y derecho de Z
 
print('El valor p es {}'.format(P2))


#PRUEBA T ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Establecer las muestras
b3 = datos["Damage"]

# Tamaño de la muestra
n3 = len(b3)

# Establecer la media de la muestra y la desviación estándar de la muestra
mean3, std3 = b3.mean(), b3.std(ddof=1)

# Calcular el error estándar
# Si es una prueba Z, dividirá la desviación estándar de la población por el radical n,
# pero la prueba t se debe a que la desviación estándar de la población es desconocida,
# por lo que se usa la desviación estándar de la muestra
se3 = std3 / np.sqrt(n3)

# prueba t
t3 = (mean3 - 50) / se3

print('t estadística es {}'.format(t3))

# Valor P
P3 = stats.t.cdf(t3, df= n3-1)

print('El valor p es {}'.format(P3))


#PRUEBA DE RELACION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Proporción de muestra
hgcount = datos['Gun-Type'].count()['HG']
totalcount = datos['index_Tdoll']

p4 = hgcount / totalcount

# Proporción general
pi_0 = 0.5

# Tamaño de la muestra
n4 = 332

# Estadísticas Z
Z4 = (p4 - pi_0) / np.sqrt(pi_0 * (1 - pi_0) / n4)

print("Estadísticas Z {}".format(Z4))

P4 = stats.norm.cdf(Z4)  # sf es el área de la derecha, cdf es el área de la izquierda

print('Valor p {}'.format(P4))
