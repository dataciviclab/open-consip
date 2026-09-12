"""Mercato PA — CONSIP vs ANAC: imprese dual-use."""

import streamlit as st
import plotly.express as px
import pandas as pd
from lab_connectors.formatters import fmt_num, fmt_pct
from sources import load_mart

st.title("🔄 Mercato PA — CONSIP vs ANAC")

SLUG = "consip_anac_imprese"

df_mercato = load_mart(SLUG, "mart_analisi_mercato", 2026)
df_imprese = load_mart(SLUG, "mart_imprese_dual_use", 2026)

if df_mercato.empty or df_imprese.empty:
    st.warning("Compose non ancora eseguito. Esegui prima: `toolkit run -c compose/consip-anac-imprese/dataset.yml`")
    st.stop()

# ── KPI globali ────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1:
    tot = int(df_imprese["partita_iva"].nunique())
    st.metric("Imprese totali", fmt_num(tot))
with k2:
    dual = int(df_imprese[df_imprese["profilo"] == "dual_use"]["partita_iva"].nunique())
    st.metric("Dual-use", fmt_num(dual))
with k3:
    solo_c = int(df_imprese[df_imprese["profilo"] == "solo_consip"]["partita_iva"].nunique())
    st.metric("Solo CONSIP", fmt_num(solo_c))
with k4:
    solo_a = int(df_imprese[df_imprese["profilo"] == "solo_anac"]["partita_iva"].nunique())
    st.metric("Solo ANAC", fmt_num(solo_a))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Distribuzione profili")
    profili = df_imprese.groupby("profilo", as_index=False)["partita_iva"].nunique().rename(columns={"partita_iva": "n"})
    fig = px.pie(profili, names="profilo", values="n",
                 title="Dual-use vs Solo CONSIP vs Solo ANAC",
                 color_discrete_map={"dual_use": "#2ecc71", "solo_consip": "#3498db", "solo_anac": "#e74c3c"})
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("% Dual-use per regione")
    df_plot = df_mercato.sort_values("pct_dual_use", ascending=True).tail(10)
    fig = px.bar(df_plot, x="pct_dual_use", y="regione", orientation="h",
                 title="Top 10 regioni per % dual-use",
                 labels={"pct_dual_use": "% Dual-use", "regione": ""})
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

st.divider()

# ── Top imprese dual-use ──────────────────────────────────────────
st.subheader("Top imprese dual-use per aggiudicazioni")
df_top = df_imprese[df_imprese["profilo"] == "dual_use"].sort_values("totale_aggiudicazioni", ascending=False).head(15)
st.dataframe(df_top[["denominazione", "regione_sede", "agg_consip", "agg_anac", "totale_aggiudicazioni", "indice_diversificazione"]],
             use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it + datiuslavoro.giustizia.it · CC BY 4.0")
