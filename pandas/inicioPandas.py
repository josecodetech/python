import pandas as pd
import numpy as np
# Series
etiquetas = ['a', 'b', 'c', 'd', 'e']
datos = np.arange(4, 9)
serie = pd.Series(datos, index=etiquetas)
print(serie)
# acceder valor
print(serie['c'])
# datos distinto tipo
datos = ['Jose', 49, 'Mar', 46]
serie = pd.Series(datos)
print(serie)
# datos directos
serie = pd.Series([1000, 500, 1200, 700], ['Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie)
# operacion suma
serie1 = pd.Series([1000, 500, 1200, 700], [
                   'Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie1)
serie2 = pd.Series([1050, 1500, 2200, 900], [
                   'Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie2)
serie3 = serie1 + serie2
print(serie3)

# dataframes
filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columnas = ['articulo1', 'articulo2', 'articulo3']
datos = [[np.nan, 100, 200], [np.nan, 100, 300],
         [300, np.nan, 400], [400, 100, 500]]

dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)
# seleccion fila
print(dataframe.loc['tienda2'])
print(dataframe.loc[['tienda2', 'tienda3']])
# seleccion columna
print(dataframe['articulo3'])
# valor concreto
print(dataframe.loc['tienda2', 'articulo3'])
# nueva columna
dataframe['articulo4'] = 25
print(dataframe)
dataframe['total'] = dataframe['articulo1']+dataframe['articulo2'] + \
    dataframe['articulo3']+dataframe['articulo4']
print(dataframe)
# eliminar columna
#dataframe = dataframe.drop(['total'], axis=1)
print(dataframe.drop(['total'], axis=1, inplace=True))
print(dataframe)
condicion = dataframe > 200
print(dataframe[condicion])
condicion = (dataframe['articulo1'] >= 200) | (dataframe['articulo2'] >= 100)
print(dataframe[condicion])
nuevaColumna = '1 2 3 4'.split()
dataframe['indices'] = nuevaColumna
print(dataframe)
dataframe = dataframe.set_index('indices')
print(dataframe)
#dataframe.dropna(axis=1, inplace=True)
#dataframe.fillna(value=90, inplace=True)
media = dataframe.mean()
print(f"La media es igual a {media}")
dataframe.fillna(value=media, inplace=True)
print(dataframe)
# union de dataframes
data1 = dataframe.copy()
data2 = dataframe.copy()
print(data1)
print(data2)
dataTotal = pd.concat([data1, data2])
print(dataTotal)
print(dataTotal['articulo3'].unique())
print(dataTotal['articulo3'].value_counts())
dataTotal = dataTotal.apply(lambda x: x*3)
print(dataTotal)
print(dataTotal.columns)
print(dataTotal.index)
print(dataTotal.sort_values(['articulo3']))
print(dataTotal.describe())

# dataTotal.to_csv('dataTotal.csv')
dataframe = pd.read_csv('dataTotal.csv', index_col=0)
print(dataframe)
