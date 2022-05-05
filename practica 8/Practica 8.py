#PRACTICA 8 / Clustering simple
#FUE REALIZADO EN UN JUPYTER NOTEBOOK PORQUE TUVE PROBLEMAS CON LAS LIBRERIAS QUE NO ESTAN EN PATH
#EN MI COMPUTADORA
#GRAFICOS GENERADOS: LOS GUARDE PARA QUE SE PUEDAN VER LA EVIDENCIA

import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from scipy.stats import mode
from sklearn.cluster import KMeans

from google.colab import drive
drive.mount("/content/gdrive")

datos = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/Characters_GF_V1.3.csv')

drop_cols = ['Index_Tdoll', 'Role_T-doll', 'Time_Production', 'Obtain_by']
df = datos.drop(columns = drop_cols)
df.head()

# k means
kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(df[['ACC', 'R_o_F']])# get centroids
centroids = kmeans.cluster_centers_
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]

## add to df
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})# define and map colors
colors = ['#DF2020', '#81DF20', '#2095DF']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})

plt.scatter(df.ACC, df.R_o_F, c=df.c, alpha = 0.6, s=10)