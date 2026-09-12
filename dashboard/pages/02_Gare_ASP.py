"""Gare ASP — Analisi delle gare Application Service Provider."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num, fmt_eur, fmt_pct
from sources import load_mart, YEARS_GARE

st.title("🏗️ Gare ASP")

# ── Filtri ─────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)
with col2:
    df_raw = load_mart("consip_gare_asp", "mart_gare_per_territorio", year)
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
k1, k2, k3 = st.columns(3)
with k1:
    st.metric("Gare totali", fmt_num(int(df["n_gare"].sum())))
with k2:
    st.metric("Valore aggiudicato", fmt_eur(float(df["valore_aggiudicato_totale"].sum())))
with k3:
    forn = float(df["n_fornitori_medio"].mean())
    st.metric("Fornitori medi", f"{forn:.1f}")

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Gare per stato")
    if "stato_gara" in df.columns:
        df_stato = df.dropna(subset=["stato_gara"]).groupby("stato_gara", as_index=False).agg(n=("n_gare", "sum"))
        fig = px.pie(df_stato, names="stato_gara", values="n", title="Distribuzione stato gare")
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Gare per provincia")
    if "provincia_pa" in df.columns:
        df_prov = df.dropna(subset=["provincia_pa"]).groupby("provincia_pa", as_index=False).agg(
            n=("n_gare", "sum"),
            valore=("valore_aggiudicato_totale", "sum"),
        ).sort_values("n", ascending=True).tail(10)
        fig = px.bar(df_prov, x="n", y="provincia_pa", orientation="h",
                     title="Top 10 province per numero gare",
                     labels={"n": "N. gare", "provincia_pa": ""})
        fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, width="stretch")

# ── Tabella dettaglio ──────────────────────────────────────────────
st.subheader("Dettaglio per provincia")
if "provincia_pa" in df.columns:
    df_tab = df.dropna(subset=["provincia_pa"]).groupby(["provincia_pa", "regione_pa"], as_index=False).agg(
        n_gare=("n_gare", "sum"),
        base_asta=("base_asta_totale", "sum"),
        valore_agg=("valore_aggiudicato_totale", "sum"),
        fornitori=("n_fornitori_medio", "mean"),
    )
    df_tab = df_tab.sort_values("valore_agg", ascending=False)
    st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
