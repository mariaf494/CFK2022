import numpy as np
import pandas as pd
df = pd.read_excel('market-price.xlsx',header=None)
df.shape
df.head() #para ver las primeras filas
df.tail() #para ver las últimas filas, si colocas (x), te muestra x filas
df.columns=['Timestamp','Price']
df.info() #para conocer si hay espacios vacíos
df['Timestamp'] = pd.to_datetime(df['Timestamp']) #para convertirlo a fecha
df.dtypes
df.set_index('Timestamp', inplace=True) #para convertirlo en el index
df.loc['2017-09-29']

bitcoin = pd.read_excel(
    'market-price.xlsx', #cargar los datos
    sheet_name='Hoja1',
    header=None, #primera fila no es el header
    names=['Timestamp', 'Price'], #coloca estos nombres de columnas
    index_col=0, #la primera columna es el index
    parse_dates=True #esa columna representa fechas
)

bitcoin.plot()
#plt.hist(marvel_df.first_appearance) para hacer un histograma

ether = pd.read_excel(
    'market-price.xlsx', #cargar los datos
    sheet_name='Hoja2', 
    index_col=0, #la primera columna es el index
    parse_dates=True #esa columna representa fechas
)

ether= ether.drop('UnixTimeStamp',axis=1) #Para eliminar esa columna
#marvel_df.loc['Vision', 'first_appearance'] = 1964 
#Vision es el index, first_appearance es la columna (Para cambiar el valor)

#marvel_df['years_since'] = 2018 - marvel_df['first_appearance']
#para agregar una nueva columna

#mask = marvel_df['sex'] == 'male' (para que solo muestre los hombres)
#mask es un boolean array

#mask = (marvel_df['sex'] == 'female') & (marvel_df['first_appearance'] > 1970)
#muestra both female an first appearance

#marvel_df.first_appearance.min()  .mean()

price=bitcoin

price['ether']= ether['Value']
price.columns=['Bitcoin','Ether']
price.info()

#CLENAING DATA

#1. Finding missing data
#2. Fixing/identify missing data

a = pd.Series(np.array([1, 7, np.nan, 3, np.nan, 4]))
b=a.mean() #el valor NaN lo vuelve cero
c=a.sum()

#pd.isna(np.nan) para detectar espacios vacío
#pd.isnull(None)

h=np.array([1, 2, 3])
x1=pd.isnull(a) #array con posiciones true/false
x2=pd.isnull(a).sum()  #int (notnull)

a.dropna() #para eliminar los datos nulos
#=price.dropna() #borra todas las filas que tengan NaN
#df.dropna(axis=1) #para eliminar columnas que tengan NaN

price=price.dropna(how='all') #Elimina fila/columna que tenga TODOS los values NaN
#price=price.dropna(thresh=50,axis=0) #minimun number of rows/columns to be kept

#a=a.fillna(0)

#a= a.fillna(method='ffill') si el primer dato es npnan, entonces lo deja npnan
#porque no tiene un valor anterior para llenarlo
#a.fillna(method='bfill') 

#(method='ffill', axis=0[o 1]) Eso determina si se llena por columna/fila

#when the value exists, but is invalid

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})

#donc, sex accepte seulement M et F comment une réponse

#df['Sex'].unique() #qué clases encuentra
#df['Sex'].value_counts() #cuántos datos asociados a clases hay

df['Sex'].replace({'D': 'F', '?': 'M'}) #para reemplazar
df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
}) #para reemplazar todo al mismo tiempo

#edades que se les fueron un 0
df.loc[df['Age']>100, 'Age']=df.loc[df['Age']>100,'Age']/10

#Duplicados
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
]) #index es el gobernador
    
#ambassadors.duplicated() boolean array, by default the first isn't a duplicate
#ambassadors.duplicated(keep='last') considera el último como isn't a duplicate

ambassadors.duplicated(keep=False) #todos los index cuyo país se repite, se vuelven TRUE

#ambassadors.drop_duplicates()
#ambassadors.drop_duplicates(keep='last')

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})

players.duplicated() #solo mostrará filas que estén completamente iguales, si hay un mismo nombre, pero distinta posición, dirá que no está duplicado
players.duplicated(subset=['Name']) #para que considere duplicado los que tengan el mismo nombre

players=players.drop_duplicates(subset=['Name'])

#para separar los valores
df10 = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

df10=df10['Data'].str.split('_', expand=True) #para volverlo un dataframe

df10.columns=['Year','Sex','Country','Number of children']

df['Year'].str.contains('\?') #datos que tengan un ?
#df['Country'].str.contains('U') #for regular letters

#for removing blank spaces
df['Country'].str.strip()
df['Country'].str.replace(' ', '')

df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'))