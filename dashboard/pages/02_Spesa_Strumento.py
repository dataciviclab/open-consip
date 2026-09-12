"""Spesa per Strumento — Convenzioni, MePA, AQ a confronto."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur
from sources import load_mart, YEARS_GARE, YEARS_CONSUMI

st.title("💰 Spesa per Strumento")

# ── Filtri ─────────────────────────────────────────────────────────
year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)

# ── Carica dati ────────────────────────────────────────────────────
df_conv = load_mart("consip_ordini_convenzione", "mart_spesa_per_convenzione", year)
df_mepa = load_mart("consip_ordini_mepa", "mart_ordini_mepa_per_bene", year)
df_util = load_mart("consip_consumi_convenzione", "mart_spesa_per_territorio", year)

# ── KPI confronto ──────────────────────────────────────────────────
k1, k2, k3 = st.columns(3)
with k1:
    spesa_conv = float(df_conv["importo_totale"].sum()) if not df_conv.empty else 0
    st.metric("Spesa Convenzioni", fmt_eur(spesa_conv))
with k2:
    spesa_mepa = float(df_mepa["valore_ordini"].sum()) if not df_mepa.empty else 0
    st.metric("Spesa MePA", fmt_eur(spesa_mepa))
with k3:
    spesa_util = float(df_util["spesa_totale"].sum()) if not df_util.empty else 0
    st.metric("Spesa Utility", fmt_eur(spesa_util))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Distribuzione spesa per strumento")
    data = []
    if spesa_conv > 0:
        data.append({"Strumento": "Convenzioni", "Spesa": spesa_conv})
    if spesa_mepa > 0:
        data.append({"Strumento": "MePA", "Spesa": spesa_mepa})
    if spesa_util > 0:
        data.append({"Strumento": "Utility (sotto-convenzione)", "Spesa": spesa_util})
    if data:
        import pandas as pd
        df_bar = pd.DataFrame(data)
        fig = px.pie(df_bar, names="Strumento", values="Spesa",
                     title="Composizione spesa per strumento")
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Spesa MePA per Beni vs Servizi")
    if not df_mepa.empty:
        fig = px.pie(df_mepa, names="bando_mepa", values="valore_ordini",
                     title="Beni vs Servizi su MePA")
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

# ── Dettaglio regioni ──────────────────────────────────────────────
st.subheader("Spesa per regione e strumento")
df_regione = load_mart("consip_ordini_mepa", "mart_ordini_mepa_per_regione", year)
if not df_regione.empty:
    df_plot = df_regione.sort_values("valore_ordini", ascending=True).tail(10)
    fig = px.bar(df_plot, x="valore_ordini", y="regione_pa", orientation="h",
                 title="Top 10 regioni per spesa MePA",
                 labels={"valore_ordini": "Valore (€)", "regione_pa": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

st.caption("Dati: dati.consip.it · CC BY 4.0")
