import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as pt

data = pd.read_csv('avocado.csv')

# 1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos
print(data.info)
# 1. End
# ---------------------------------------------------------------------------
# 2. Mostrar los primeros 100 registros
print(data.head(100))
# 2. End
# ---------------------------------------------------------------------------
# 3. Mostrar los últimos 20 registros
print(data.tail(20))
# 3. End
# # ---------------------------------------------------------------------------
# 4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos
print('Precio Minimo', data['AveragePrice'].min())
print('Precio Promedio', data['AveragePrice'].mean())
print('Precio Maximo', data['AveragePrice'].max())
# 4. End
# # ---------------------------------------------------------------------------
# 5.Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija,) 
Grafico = pt.subplot()

Albany = data[data['region']=='Albany']
Baltimore = data[data['region']=='BaltimoreWashington']
Boise = data[data['region']=='Boise']

Albany = Albany.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'red', ax = Grafico)

Baltimore = Baltimore.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'blue', ax = Grafico)

Boise = Boise.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'green', ax = Grafico)

pt.show()
# 5. End