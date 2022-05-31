#!/usr/bin/env python3
import pickle

import pandas as pd
import numpy as np

from pathlib import Path
from datetime import datetime

import sys
temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('log_directivos.txt', 'w') # redirect all prints to this log file

## Estudiantes

ruta =Path(__file__).parent


sheet_id = "1AtmDU6E8D4nGg8149FVUfRQrax90w1lR9OlgQM9fHeU"
sheet_name = "Respuestas de formulario 1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
url = url.replace(" ", "%20")

df0=pd.read_csv(url)

with open(ruta/'columnas_directivos.pkl', 'rb') as handle:
    dict_col_est = pickle.load(handle)

df0 = df0.rename(columns=dict_col_est)
df0 = df0.drop(columns=df0.filter(regex=r'eliminar').columns)
df0['Timestamp'] = pd.to_datetime(df0['Timestamp'])
df0['Fecha'] = df0.Timestamp.dt.strftime('%d/%m')

df0['N registro']=df0.index
df4=df0.copy()
df4['Instrumento']="Encuesta Directivos"
df4=df4.dropna(subset=['Código IE'],inplace=False)
df4=df4.dropna(subset=['ID'],inplace=False)
print(df4.head())
df4 = df4[df4['N registro']>2]
#df4 = df4[df4.Timestamp>'2022-04-14']


df4 = df4.drop(columns='Timestamp')

df4['Código IE']=df4['Código IE'].astype(int)
df4=df4[df4['Código IE'] > 0]
df4=df4[df4['Código IE']<253]
df4['Código IE']=df4['Código IE'].astype(str)
df4['Código IE']=df4['Código IE'].str.zfill(3)
print('Cantidad de códigos IE después de filtrar mayor y menor ',len(df4['Código IE'].unique()))
print('Códigos que se mantienen: ',df4['Código IE'].unique())


df4= df4[df4['ID'] >= 1000000]
df4= df4[df4['ID'] < 3000000000] #quedan 156
df4=df4.dropna(subset=['ID'],inplace=False)

print('columnas: ', df4.columns.tolist())

new_index= ['N registro', 'Instrumento', 'Fecha','Política de datos', 'ID',
 'Edad', 'Sexo', 'Cabeza de hogar', 'Estado civil', 'Líder comunitario',
 'Formación STEM', 'Rol en IE', '¿En su institución hay estudiantes con algún tipo de discapacidad?',
'Estudiantes  con discapacidad intelectual',
'Estudiantes con Discapacidad física o motora',
'Estudiantes con Discapacidad auditiva', 'Estudiantes con Discapacidad visual',
'Estudiantes con Discapacidad psicosocial', 'Estudiantes con Discapacidad múltiple',
'Estudiante con Trastornos Específicos del Aprendizaje',
'Considera importante enseñar el pensamiento computacional desde los primeros niveles educativos',
 'Conceptos que deben incluirse en la clase de tecnología e informática',
 'Comentarios autorreporte',
'1.1 Los maestros de esta Institución educativa incorporan el pensamiento computacional en sus clases',
'1.2 Los esfuerzos de los maestros para enseñar conceptos de pensamiento computacional son muy valorados en esta institución educativa', '1.3 Animo a los maestros de otras disciplinas a asistir a oportunidades de desarrollo profesional enfocadas en pensamiento computacional.', '1.4 Hay alguien en mi colegio que puede asesorar a los estudiantes sobre los caminos hacia una carrera en STEM', '1.5 En los próximos tres años, espero que la cantidad de oportunidades para aprender sobre pensamiento computacional en este colegio aumenten', '1.6 Es extremadamente importante que todos los estudiantes aprendan pensamiento computacional.', '1.7 Tener educación en pensamiento computacional mejoraría significativamente las futuras opciones de carrera para los estudiantes de mi escuela.', '1.8 El pensamiento computacional se utiliza en muchos tipos diferentes de trabajos.', '1.9 Ofrecer oportunidades para aprender de pensamiento computacional tiene el mismo valor o más para el éxito futuro de un estudiante que otros cursos obligatorios como matemáticas, biología, ciencias sociales, historia e inglés', '1.10 Conozco y puedo recomendar a mis estudiantes diferentes programas de formación relacionadas al pensamiento computacional y/o ciencias de la computación', '1.11 Los estudiantes reciben asesoría vocacional sobre alternativas u oportunidades relacionadas a carreras STEM', '1.12 Informo a mis estudiantes sobre oportunidades que existen para continuar los estudios en áreas relacionadas al pensamiento computacional y/o ciencias de la computación', 'Comentarios autodiagnóstico', 'Actividades que se promueven en esta institución educativa para apoyar la formación docente enfocadas en pensamiento computacional', '¿La rotación de los docentes de tecnología e informática influye sobre la calidad y el aprendizaje del área de los estudiantes en los diferentes grados?', 'Código IE', 'Tipo de ID', 'Número de estudiantes matriculados', 'Número de docentes que laboran']

df0=df0.reindex(new_index, axis='columns')
df4=df4.reindex(new_index, axis='columns')

registroseliminados=set(df0['N registro']).difference(set(df4['N registro']))
dfe=df0[df0['N registro'].isin(registroseliminados)]


archivo_eliminados = "eliminados/Eliminados_directivos.xlsx"
archivo_eliminados = ruta/archivo_eliminados

archivo_descargable = ruta.parent.parent.parent/"data/descargables/DirectivosCFK.xlsx"
dfe.to_excel(archivo_eliminados, index=False)
df4.to_excel(archivo_descargable,index=False)
print('Publicados ', df4.shape)
print('Eliminados ', dfe.shape)
sys.stdout.close()                # ordinary file object
sys.stdout = temp
