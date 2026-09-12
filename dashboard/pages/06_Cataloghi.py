"""Cataloghi — Cosa si compra su Consip."""

import streamlit as st
import plotly.express as px
from lab_connectors.formatters import fmt_num
from sources import load_mart, YEARS_GARE

st.title("🛒 Cosa si compra su Consip")

# ── Filtri ─────────────────────────────────────────────────────────
year = st.selectbox("Anno", YEARS_GARE, index=len(YEARS_GARE) - 1)

df = load_mart("consip_cataloghi", "mart_cataloghi_per_categoria", year)

if df.empty:
    st.warning("Nessun dato cataloghi disponibile.")
    st.stop()

# ── KPI ────────────────────────────────────────────────────────────
k1, k2 = st.columns(2)
with k1:
    n_prod = int(df["n_prodotti"].sum())
    st.metric("Prodotti totali", fmt_num(n_prod))
with k2:
    n_cat = int(df["categoria_merceologica"].nunique())
    st.metric("Categorie", fmt_num(n_cat))

st.divider()

# ── Grafici ────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Prodotti per categoria merceologica")
    df_plot = df.sort_values("n_prodotti", ascending=True).tail(10)
    fig = px.bar(df_plot, x="n_prodotti", y="categoria_merceologica", orientation="h",
                 title="Top 10 categorie per numero prodotti",
                 labels={"n_prodotti": "N. prodotti", "categoria_merceologica": ""})
    fig.update_layout(height=500, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

with col_right:
    st.subheader("Prodotti per tipo strumento")
    df_tipo = df.groupby("tipo_strumento", as_index=False).agg(
        n_prodotti=("n_prodotti", "sum"),
    ).sort_values("n_prodotti", ascending=True)
    fig = px.pie(df_tipo, names="tipo_strumento", values="n_prodotti",
                 title="Distribuzione per tipo strumento")
    fig.update_layout(height=500, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, width="stretch")

# ── Tabella dettaglio ──────────────────────────────────────────────
st.subheader("Dettaglio per categoria")
df_tab = df.groupby(["tipo_strumento", "categoria_merceologica"], as_index=False).agg(
    prodotti=("n_prodotti", "sum"),
    cpv=("n_cpv_distinti", "sum"),
    lotti=("n_lotti_distinti", "sum"),
).sort_values("prodotti", ascending=False)
st.dataframe(df_tab, use_container_width=True, hide_index=True)

st.caption("Dati: dati.consip.it · CC BY 4.0")
