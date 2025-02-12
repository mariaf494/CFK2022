import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import utils.plots as plots
from utils.read_data import read_data

#pio.templates.default = "plotly_white"

import apps.pages.caracterizacion.docente as page_docente


config = plots.get_config()

def app():
    plots.plotly_settings(px)
    st.title('Consolidación')
    _type = st.selectbox('Elija el grupo que desea ver',["Estudiantes","Docentes","Directivos"])
    st.write("##")

    df = get_data(_type)

    if(_type =='Docentes'):
        page_docente.app(df)    
    

# Helpers

def get_data(name):
    if (name == 'Estudiantes'):
        return read_data('est_sociodemo')
    if (name == 'Directivos'):
        return read_data('dir_sociodemo')
    if (name == 'Docentes'):
        return read_data('doc_sociodemo')

