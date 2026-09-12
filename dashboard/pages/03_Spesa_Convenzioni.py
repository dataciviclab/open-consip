"""Spesa Convenzioni — Analisi della spesa per utility e ordini."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur
from sources import load_mart, YEARS_CONSUMI

st.title("💰 Spesa Convenzioni")

# ── Filtri ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Anno", YEARS_CONSUMI, index=len(YEARS_CONSUMI) - 1)
with col2:
    df_raw = load_mart("consip_consumi_convenzione", "mart_spesa_per_territorio", year)
    regioni = ["Tutte"] + sorted([x for x in df_raw["regione_pa"].dropna().unique().tolist()]) if not df_raw.empty else ["Tutte"]
    regione = st.selectbox("Regione", regioni)

# ── Filtraggio ─────────────────────────────────────────────────────
df = df_raw.copy()
if regione != "Tutte":
    df = df[df["regione_pa"] == regione]

if df.empty:
    st.warning("Nessun dato disponibile per i filtri selezionati.")
    st.stop()

# ── KPI ────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1:
    spesa = float(df["spesa_totale"].sum())
    st.metric("Spesa totale", fmt_eur(spesa))
with k2:
    ordini = int(df["ordini_totali"].sum())
    st.metric("Ordini totali", fmt_num(ordini))
with k3:
    pa = int(df["pa_coinvolte"].sum())
    st.metric("PA coinvolte", fmt_num(pa))
with k4:
    convenzioni = int(df["convenzioni_distinte"].sum())
    st.metric("Convenzioni", fmt_num(convenzioni))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Spesa per tipologia PA")
    if "tipologia_amministrazione" in df.columns:
        df_tip = df.groupby("tipologia_amministrazione", as_index=False).agg(
            spesa=("spesa_totale", "sum"),
        ).sort_values("spesa", ascending=True).tail(10)
        fig = px.bar(df_tip, x="spesa", y="tipologia_amministrazione", orientation="h",
                     title="Top 10 tipologie PA per spesa",
                     labels={"spesa": "Spesa (€)", "tipologia_amministrazione": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Spesa per regione fornitore")
    if "regione_fornitore" in df.columns:
        df_forn = df.groupby("regione_fornitore", as_index=False).agg(
            spesa=("spesa_totale", "sum"),
        ).sort_values("spesa", ascending=True).tail(10)
        fig = px.bar(df_forn, x="spesa", y="regione_fornitore", orientation="h",
                     title="Top 10 regioni fornitore",
                     labels={"spesa": "Spesa (€)", "regione_fornitore": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

# ── Tabella dettaglio ──────────────────────────────────────────────
st.subheader("Dettaglio per regione PA")
if "regione_pa" in df.columns:
    df_tab = df.groupby("regione_pa", as_index=False).agg(
        spesa=("spesa_totale", "sum"),
        ordini=("ordini_totali", "sum"),
        pa=("pa_coinvolte", "sum"),
        convenzioni=("convenzioni_distinte", "sum"),
    ).sort_values("spesa", ascending=False)
    st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
