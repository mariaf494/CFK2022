import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils.read_data import read_data
#pio.templates.default = "plotly_white"

px.defaults.template = "plotly_white"
px.color_discrete_sequence= px.colors.qualitative.Set2
px.defaults.width = 600
px.defaults.height = 400

def main():

    df = read_data('doc_sociodemo')
    st.write("Fecha de actualización", df.Fecha.max())
    st.metric("Número de docentes", len(df.ID.unique()))
    col1, col2= st.columns(2)

    pivot_1 = pd.pivot_table(df, index='Sexo', values='ID', aggfunc='nunique').reset_index()
    fig_1 = px.bar(pivot_1, x='Sexo', y ='ID',  color='Sexo', color_discrete_sequence= px.colors.qualitative.Set2)
    col1.plotly_chart(fig_1)
    pivot_2 = pd.pivot_table(df, index=['Formado tecnología e informática','Sexo'],values='ID', aggfunc='nunique').reset_index()
    fig_2 = px.bar(pivot_2, y='ID', x='Formado tecnología e informática', color='Sexo', barmode='group',  color_discrete_sequence= px.colors.qualitative.Set2)
    col2.plotly_chart(fig_2)
    st.markdown("### Docentes de tecnología e informática")
    st.write('Estadísticas')

def app():
    st.title('Tablero')
    main()
