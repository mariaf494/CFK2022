#!/usr/bin/env python3
import pickle

import pandas as pd
import numpy as np

from pathlib import Path
from datetime import datetime

import sys
temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('log_pivot.txt', 'w') # redirect all prints to this log file

## Estudiantes

ruta =Path(__file__).parent
archivo_descargable = ruta.parent.parent.parent/"data/descargables/"
print(ruta)
df = pd.DataFrame(columns=['N registro','Instrumento','Código IE','ID'])

columnas_pivot = set(df.columns)
archivos = list(archivo_descargable.glob("*.xlsx"))
df_temp=pd.read_excel(archivos[0])
for file in archivos:
    df_temp = pd.read_excel(file)
    if len(columnas_pivot.difference(set(df_temp.columns))) > 0:
        print('Error!! ', file.name)
        print(columnas_pivot.difference(set(df_temp.columns)))
    else:
        df = pd.concat([df,df_temp],ignore_index=True, join='inner')

print(df.head())

pivot = df.pivot_table(index='Código IE',columns='Instrumento', values='ID', aggfunc= 'count')
pivot=pivot.reset_index()
print('Tamaño pivot', pivot.shape)

pivot=pivot.fillna(0)
pivot['Fecha'] =pd.Timestamp.today()
pivot['Fecha']=pivot['Fecha'].dt.strftime("%d-%m-%Y")

archivo_pivot = ruta.parent.parent.parent/"data/InstrumentosCFK.xlsx"
pivot.to_excel(archivo_pivot)
sys.stdout.close()                # ordinary file object
sys.stdout = temp
