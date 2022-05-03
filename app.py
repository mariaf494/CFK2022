# Import streamlit
import streamlit as st


# Import each page file
from apps import inicio
from apps import dashboard_cons



PAGES = {
    "Inicio": inicio,
    "Caracterización Inicial": dashboard_cons
}


def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("CFK 2022")
    pag = st.sidebar.radio("Página: ", list(PAGES.keys()))

    PAGES[pag].app()


if __name__ == "__main__":
    main()
