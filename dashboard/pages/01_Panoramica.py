"""Panoramica — Visione d'insieme sull'acquisto pubblico italiano."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur
from sources import load_mart, YEARS_GARE, YEARS_CONSUMI

st.title("📊 Open CONSIP — Panoramica")

year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)

df_gare = load_mart("consip_gare_asp", "mart_gare_per_territorio", year)
df_spesa = load_mart("consip_consumi_convenzione", "mart_spesa_per_territorio", year)
df_imprese = load_mart("consip_operatori_economici", "mart_imprese_per_territorio", year)
df_mePA = load_mart("consip_ordini_mepa", "mart_ordini_mepa_per_bene", year)
df_conv = load_mart("consip_ordini_convenzione", "mart_spesa_per_convenzione", year)

# ── KPI ────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1:
    spesa_mepa = float(df_mePA["valore_ordini"].sum()) if not df_mePA.empty else 0
    st.metric("Spesa MePA", fmt_eur(spesa_mepa))
with k2:
    spesa_conv = float(df_conv["importo_totale"].sum()) if not df_conv.empty else 0
    st.metric("Spesa Convenzioni", fmt_eur(spesa_conv))
with k3:
    n_gare = int(df_gare["n_gare"].sum()) if not df_gare.empty else 0
    st.metric("Gare ASP", fmt_num(n_gare))
with k4:
    n_imprese = int(df_imprese["n_imprese"].sum()) if not df_imprese.empty else 0
    st.metric("Imprese attive", fmt_num(n_imprese))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Spesa per strumento")
    data = []
    if spesa_mepa > 0:
        data.append({"Strumento": "MePA", "Spesa": spesa_mepa})
    if spesa_conv > 0:
        data.append({"Strumento": "Convenzioni", "Spesa": spesa_conv})
    spesa_util = float(df_spesa["spesa_totale"].sum()) if not df_spesa.empty else 0
    if spesa_util > 0:
        data.append({"Strumento": "Utility", "Spesa": spesa_util})
    if data:
        import pandas as pd
        df_bar = pd.DataFrame(data)
        fig = px.pie(df_bar, names="Strumento", values="Spesa",
                     title="Composizione spesa per strumento")
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Gare ASP per regione")
    if not df_gare.empty:
        df_plot = df_gare.dropna(subset=["regione_pa"]).groupby("regione_pa", as_index=False).agg(
            valore=("valore_aggiudicato_totale", "sum"),
        ).sort_values("valore", ascending=True).tail(10)
        fig = px.bar(df_plot, x="valore", y="regione_pa", orientation="h",
                     title="Top 10 regioni per valore aggiudicato",
                     labels={"valore": "Valore (€)", "regione_pa": ""})
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

st.caption("Dati: dati.consip.it · CC BY 4.0")
