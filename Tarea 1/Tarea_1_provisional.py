import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

#matplotlib inline
sns.set(style='white')

#Habrimos el archivo y analizamos la cabeza de los datos para ver los tipos
terremotos = pd.read_csv(r'C:\Users\lucia\OneDrive\Escritorio\U\terremotos.csv')
print(terremotos.head())

#Analizamos los datos que estén en blanco
nulos = terremotos.isnull().sum()
print(nulos)

#Ahora analizamos los tipos de datos que tenemos en el archivo mediante gráficos de barras
#plt.figure(figsize=(10, 6)) #Figura de magnitud
#sns.countplot(data=terremotos, x='mag', color='m')
#plt.xlabel('Magnitud')
#plt.ylabel('Cantidad de Terremotos')
#plt.title('Distribución de Terremotos por Magnitud')
#plt.grid(True)

#plt.show()

#plt.figure(figsize=(10, 6)) #Figura de nst
#sns.countplot(data=terremotos, x='nst', color='c')
#plt.xlabel('Número de Estaciones')
#plt.ylabel('Cantidad de Terremotos')
#plt.title('Distribución de Terremotos por Número de Estaciones')
#plt.grid(True)

#plt.show()

#plt.figure(figsize=(10, 6)) #Figura de net
#sns.countplot(data=terremotos, x='net', color='m')
#plt.xlabel('Red Sísmica')
#plt.ylabel('Cantidad de Terremotos')
#plt.title('Distribución de Terremotos por Red Sísmica')
#plt.grid(True)

#plt.show()

#plt.figure(figsize=(10, 6)) #Figura de tipo rms
#sns.countplot(data=terremotos, x='rms', color='c')
#plt.xlabel('RMS')
#plt.ylabel('Cantidad de Terremotos')
#plt.title('Distribución de Terremotos por RMS')
#plt.grid(True)

#plt.show()

fig = px.scatter_geo(terremotos, lat='latitude', lon='longitude', color='mag', title='Distribución de Terremotos en el Mundo')
fig.write_html(r"C:\Users\lucia\OneDrive\Escritorio\U\mapa_terremotos.html")

#Ahora analizaremos la tendencia de los terremotos por fecha 
terremotos['time'] = pd.to_datetime(terremotos['time']) #generamos fechas a partir de la columna time
terremotos['year'] = terremotos['time'].dt.year #generamos una columna con el año de cada terremoto

terremotos['mag_cat'] = pd.cut(terremotos['mag'], bins=[0, 6, 7, 10], labels=['<6', '6-7', '7+']) #organizamos los terremotos por magnitud en categorías

conteo = terremotos.groupby(['year', 'mag_cat']).size().reset_index(name='cantidad') # agrupamos los datos por año y categoría de magnitud, y contamos la cantidad de terremotos en cada grupo

#plt.figure(figsize=(14,6)) #Figura de cantidad de terremotos por año y magnitud 
#sns.pointplot(data=conteo, x='year', y='cantidad', hue='mag_cat')
#plt.title('Cantidad de terremotos por año, según magnitud')
#plt.xlabel('Año')
#plt.ylabel('Cantidad de Terremotos')
#plt.grid(True)

#plt.show() #Con esto podemos concluir que si ignoramos los de >6° se tendría un promedio

#plt.figure(figsize=(10,6))
#sns.barplot(data=conteo, x='year', y='cantidad', color='m')
#plt.title('Cantidad de terremotos por año')
#plt.xlabel('Año')
#plt.ylabel('Cantidad de terremotos')
#plt.grid(True)

#plt.show() #Con esto me dí cuenta de que hice mal la variable conteo y procedo a arreglarlo en el siguiente gráfico

terremotos_grandes = terremotos[terremotos['mag'] >= 7] #primero se filtró con 6, pero no dió el resultado deseado
conteo_grandes = terremotos_grandes.groupby('year').size().reset_index(name='cantidad')

#plt.figure(figsize=(14,6))
#sns.barplot(data=conteo_grandes, x='year', y='cantidad', color='c')
#plt.title('Cantidad de terremotos (mag >= 7) por año')
#plt.xlabel('Año')
#plt.ylabel('Cantidad de terremotos')
#plt.grid(True)

#plt.show() #Aquí se vé la tendencia que podríamos afirmar, ignora la eficacia de los sismografos actuales versus los antiguos. Por lo tanto no van en aumento solo lo detectamos más.