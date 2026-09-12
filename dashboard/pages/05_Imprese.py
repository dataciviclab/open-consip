"""Imprese — Distribuzione imprese su Consip."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num
from sources import load_mart, YEARS_GARE

st.title("🏢 Imprese")

year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)

df = load_mart("consip_operatori_economici", "mart_imprese_per_territorio", year)
if df.empty:
    st.warning("Nessun dato disponibile.")
    st.stop()

k1, k2, k3 = st.columns(3)
with k1:
    st.metric("Imprese totali", fmt_num(int(df["n_imprese"].sum())))
with k2:
    st.metric("Con aggiudicazioni", fmt_num(int(df["numero_aggiudicazioni_totale"].sum())))
with k3:
    st.metric("Con contratti attivi", fmt_num(int(df["numero_contratti_attivi_totale"].sum())))

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    df_plot = df.dropna(subset=["regione_sede_legale"]).groupby("regione_sede_legale", as_index=False).agg(
        imprese=("n_imprese", "sum"),
    ).sort_values("imprese", ascending=True).tail(10)
    fig = px.bar(df_plot, x="imprese", y="regione_sede_legale", orientation="h",
                 title="Top 10 regioni per numero imprese",
                 labels={"imprese": "N. imprese", "regione_sede_legale": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

with col_right:
    if "forma_societaria" in df.columns:
        df_forma = df.dropna(subset=["forma_societaria"]).groupby("forma_societaria", as_index=False).agg(
            imprese=("n_imprese", "sum"),
        ).sort_values("imprese", ascending=True).tail(10)
        fig = px.bar(df_forma, x="imprese", y="forma_societaria", orientation="h",
                     title="Top 10 forme societarie",
                     labels={"imprese": "N. imprese", "forma_societaria": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

st.subheader("Dettaglio per regione")
df_tab = df.dropna(subset=["regione_sede_legale"]).groupby("regione_sede_legale", as_index=False).agg(
    imprese=("n_imprese", "sum"),
    aggiudicazioni=("numero_aggiudicazioni_totale", "sum"),
    contratti=("numero_contratti_attivi_totale", "sum"),
).sort_values("imprese", ascending=False)
st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
