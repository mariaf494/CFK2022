import streamlit as st
from multiapp import MultiApp
from apps import home, dashboard_cons # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Tablero", dashboard_cons.app)
app.add_app("Home", home.app)


# The main app
app.run()
