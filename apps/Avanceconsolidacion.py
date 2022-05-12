import streamlit as st
import pandas as pd
import numpy as np
import utils.plots as plots
import plotly.express as px
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

config = plots.get_config()

#----

def app():
    st.title('Avance Consolidación 2022')
    
    tabla = pd.read_excel('data/InstrumentosCFK.xlsx', index_col=0)
    st.write('Fecha de actualización:',tabla.loc[0,'Fecha'])
    tabla2= tabla.iloc[:,:-1]
    gb = GridOptionsBuilder.from_dataframe(tabla2)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    #gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()
    
    grid_response = AgGrid(
    tabla2,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=True,
    theme= 'streamlit', #Add theme color to the table
    enable_enterprise_modules=False,
    height=400, 
    width='100%',
    reload_data=True
    )