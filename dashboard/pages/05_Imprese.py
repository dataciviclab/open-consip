"""Imprese — Analisi della distribuzione delle imprese."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num
from sources import load_mart, YEARS_GARE

st.title("🏢 Imprese")

# ── Filtri ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)
with col2:
    df_raw = load_mart("consip_operatori_economici", "mart_imprese_per_territorio", year)
    regioni = ["Tutte"] + sorted([x for x in df_raw["regione_sede_legale"].dropna().unique().tolist()]) if not df_raw.empty else ["Tutte"]
    regione = st.selectbox("Regione", regioni)

# ── Filtraggio ─────────────────────────────────────────────────────
df = df_raw.copy()
if regione != "Tutte":
    df = df[df["regione_sede_legale"] == regione]

if df.empty:
    st.warning("Nessun dato disponibile per i filtri selezionati.")
    st.stop()

# ── KPI ────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1:
    n_imprese = int(df["n_imprese"].sum())
    st.metric("Imprese totali", fmt_num(n_imprese))
with k2:
    con_agg = int(df["numero_aggiudicazioni_totale"].sum())
    st.metric("Aggiudicazioni totali", fmt_num(con_agg))
with k3:
    con_contratti = int(df["numero_contratti_attivi_totale"].sum())
    st.metric("Contratti attivi", fmt_num(con_contratti))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Imprese per regione")
    df_plot = df.groupby("regione_sede_legale", as_index=False).agg(
        imprese=("n_imprese", "sum"),
    ).sort_values("imprese", ascending=True).tail(10)
    fig = px.bar(df_plot, x="imprese", y="regione_sede_legale", orientation="h",
                 title="Top 10 regioni per numero imprese",
                 labels={"imprese": "N. imprese", "regione_sede_legale": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Distribuzione per forma societaria")
    if "forma_societaria" in df.columns:
        df_forma = df.dropna(subset=["forma_societaria"]).groupby("forma_societaria", as_index=False).agg(
            imprese=("n_imprese", "sum"),
        ).sort_values("imprese", ascending=True).tail(10)
        fig = px.bar(df_forma, x="imprese", y="forma_societaria", orientation="h",
                     title="Top 10 forme societarie",
                     labels={"imprese": "N. imprese", "forma_societaria": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

# ── Tabella dettaglio ──────────────────────────────────────────────
st.subheader("Dettaglio per regione")
df_tab = df.dropna(subset=["regione_sede_legale"]).groupby("regione_sede_legale", as_index=False).agg(
    imprese=("n_imprese", "sum"),
    aggiudicazioni=("numero_aggiudicazioni_totale", "sum"),
    contratti=("numero_contratti_attivi_totale", "sum"),
).sort_values("imprese", ascending=False)
st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
