#!/usr/bin/env python3
"""Open CONSIP · Dashboard Streamlit
Acquisti pubblici italiani: dati Consip per regione, strumento, impresa.
"""

import streamlit as st

st.set_page_config(
    page_title="Open CONSIP · Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = {
    "": [
        st.Page("pages/01_Panoramica.py", title="Panoramica", icon="📊", default=True),
    ],
    "Analisi": [
        st.Page("pages/02_Spesa_Strumento.py", title="Spesa per Strumento", icon="💰"),
        st.Page("pages/03_Mercato_PA.py", title="Mercato PA", icon="🔄"),
        st.Page("pages/04_Competizione_MePA.py", title="Competizione MePA", icon="📈"),
        st.Page("pages/05_Imprese.py", title="Imprese", icon="🏢"),
        st.Page("pages/06_Cataloghi.py", title="Cosa si compra", icon="🛒"),
    ],
    "Strumenti": [
        st.Page("pages/07_SQL.py", title="Query SQL", icon="🧪"),
    ],
}

pg = st.navigation(pages, position="sidebar")

st.sidebar.markdown("---")
st.sidebar.caption("Dati: dati.consip.it + datiuslavoro.giustizia.it (CC BY 4.0)")
st.sidebar.caption(
    "Codice: [dataciviclab/open-consip](https://github.com/dataciviclab/open-consip)"
)
st.sidebar.caption("[DataCivicLab](https://dataciviclab.org/) · CC BY 4.0")

pg.run()
