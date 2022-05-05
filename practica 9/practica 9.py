#PRACTICA 9 / Clustering classification(?)
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

plt.scatter(df.ACC, df.Damage)
plt.xlabel("Accuracy")
plt.ylabel("Damage")
plt.show()
plt.close()

# k means
kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(df[['ACC', 'Damage']])

# get centroids
centroids = kmeans.cluster_centers_
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]

## add to df
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})# define and map colors
colors = ['#ff3333', '#ffce33', '#ffff33']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})

#####PLOT#####

from matplotlib.lines import Line2D
fig, ax = plt.subplots(1, figsize=(8,8))

# plot data
plt.scatter(df.ACC, df.Damage, c=df.c, alpha = 0.6, s=10)

# plot centroids
plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)

# plot Attack mean
plt.plot([df.ACC.mean()]*2, [0,200], color='black', lw=0.5, linestyle='--')
plt.xlim(0,200)

# plot Defense mean
plt.plot([0,200], [df.Damage.mean()]*2, color='black', lw=0.5, linestyle='--')
plt.ylim(0,200)

# create a list of legend elemntes
## average line
legend_elements = [Line2D([0], [0], color='black', lw=0.5, linestyle='--', label='Average')]

## markers / records
cluster_leg = [Line2D([0], [0], marker='o', color='w', label='DMG Class {}'.format(i+1), 
               markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]

## centroids
cent_leg = [Line2D([0], [0], marker='^', color='w', label='Centroid - C{}'.format(i+1), 
            markerfacecolor=mcolor, markersize=10) for i, mcolor in enumerate(colors)]

# add all elements to the same list
legend_elements.extend(cluster_leg)
legend_elements.extend(cent_leg)

# plot legend
plt.legend(handles=legend_elements, loc='upper right', ncol=2)

# title and labels
plt.title('Offensive Tdoll Stats\n', loc='left', fontsize=22)
plt.xlabel('ACC')
plt.ylabel('Damage')
