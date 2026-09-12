"""Panoramica — Visione d'insieme sull'acquisto pubblico italiano."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur, fmt_pct
from sources import load_mart, YEARS_GARE, YEARS_CONSUMI

st.title("📊 Open CONSIP — Panoramica")

# ── Filtri ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    year_gare = st.selectbox("Anno gare", YEARS_GARE, index=len(YEARS_GARE) - 1)
with col2:
    year_spesa = st.selectbox("Anno spesa", YEARS_CONSUMI, index=len(YEARS_CONSUMI) - 1)

# ── KPI principali ─────────────────────────────────────────────────
df_gare = load_mart("consip_gare_asp", "mart_gare_per_territorio", year_gare)
df_spesa = load_mart("consip_consumi_convenzione", "mart_spesa_per_territorio", year_spesa)
df_imprese = load_mart("consip_operatori_economici", "mart_imprese_per_territorio", year_gare)
df_mePA = load_mart("consip_rdo_td_stipulate", "mart_competizione_mepa", year_gare)

k1, k2, k3, k4 = st.columns(4)

with k1:
    n_gare = int(df_gare["n_gare"].sum()) if not df_gare.empty else 0
    st.metric("Gare ASP", fmt_num(n_gare))

with k2:
    val_agg = float(df_gare["valore_aggiudicato_totale"].sum()) if not df_gare.empty else 0
    st.metric("Valore aggiudicato", fmt_eur(val_agg))

with k3:
    n_imprese = int(df_imprese["n_imprese"].sum()) if not df_imprese.empty else 0
    st.metric("Imprese attive", fmt_num(n_imprese))

with k4:
    spesa = float(df_spesa["spesa_totale"].sum()) if not df_spesa.empty else 0
    st.metric("Spesa utility", fmt_eur(spesa))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Gare ASP per regione")
    if not df_gare.empty:
        df_plot = df_gare.groupby("regione_pa", as_index=False).agg(
            n_gare=("n_gare", "sum"),
            valore=("valore_aggiudicato_totale", "sum"),
        ).sort_values("valore", ascending=True).tail(10)
        fig = px.bar(df_plot, x="valore", y="regione_pa", orientation="h",
                     title="Top 10 regioni per valore aggiudicato",
                     labels={"valore": "Valore (€)", "regione_pa": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("Nessun dato gare disponibile.")

with col_right:
    st.subheader("Spesa utility per regione")
    if not df_spesa.empty:
        df_plot = df_spesa.groupby("regione_pa", as_index=False).agg(
            spesa=("spesa_totale", "sum"),
        ).sort_values("spesa", ascending=True).tail(10)
        fig = px.bar(df_plot, x="spesa", y="regione_pa", orientation="h",
                     title="Top 10 regioni per spesa utility",
                     labels={"spesa": "Spesa (€)", "regione_pa": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("Nessun dato spesa disponibile.")

st.caption("Dati: dati.consip.it · CC BY 4.0")
