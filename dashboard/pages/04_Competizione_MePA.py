"""Competizione MePA — Analisi della competizione sul Mercato Elettronico."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur
from sources import load_mart, YEARS_GARE

st.title("📈 Competizione MePA")

# ── Filtri ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)
with col2:
    df_raw = load_mart("consip_rdo_td_stipulate", "mart_competizione_mepa", year)
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
    contratti = int(df["n_contratti"].sum())
    st.metric("Contratti stipulati", fmt_num(contratti))
with k2:
    valore = float(df["valore_contratti"].sum())
    st.metric("Valore contratti", fmt_eur(valore))
with k3:
    forn = float(df["fornitori_medi"].mean())
    st.metric("Fornitori medi", f"{forn:.1f}")
with k4:
    tempi = float(df["tempi_stipula_medio"].mean())
    st.metric("Tempi medi stipula", f"{tempi:.1f} gg")

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Contratti per regione")
    df_plot = df.groupby("regione_pa", as_index=False).agg(
        contratti=("n_contratti", "sum"),
        valore=("valore_contratti", "sum"),
    ).sort_values("valore", ascending=True).tail(10)
    fig = px.bar(df_plot, x="valore", y="regione_pa", orientation="h",
                 title="Top 10 regioni per valore contratti",
                 labels={"valore": "Valore (€)", "regione_pa": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Tempi di stipula per regione")
    df_tempi = df.groupby("regione_pa", as_index=False).agg(
        tempi=("tempi_stipula_medio", "mean"),
    ).sort_values("tempi", ascending=False).head(10)
    fig = px.bar(df_tempi, x="tempi", y="regione_pa", orientation="h",
                 title="Top 10 regioni per tempi di stipula",
                 labels={"tempi": "Giorni medi", "regione_pa": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

# ── Tabella dettaglio ──────────────────────────────────────────────
st.subheader("Dettaglio per regione")
df_tab = df.groupby("regione_pa", as_index=False).agg(
    contratti=("n_contratti", "sum"),
    valore=("valore_contratti", "sum"),
    fornitori=("fornitori_medi", "mean"),
    tempi=("tempi_stipula_medio", "mean"),
).sort_values("valore", ascending=False)
st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
