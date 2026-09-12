"""Fonti dati per la dashboard Open CONSIP.

Wrappa lab_connectors.duckdb.queries con @st.cache_data.
"""

from __future__ import annotations

import streamlit as st

from lab_connectors.duckdb.queries import (
    load_mart_table as _load_mart_table,
    query_clean as _query_clean,
)

PREFIX = "open-consip/"
YEARS_ALL = [2023, 2024, 2025, 2026]
YEARS_GARE = [2024, 2025, 2026]
YEARS_CONSUMI = [2023, 2024, 2025]


@st.cache_data(ttl=3600, show_spinner=False)
def load_mart(slug: str, table: str, year: int):
    """Carica un singolo mart table da GCS (cached 1h)."""
    return _load_mart_table(slug, table, year, prefix=PREFIX)


@st.cache_data(ttl=3600, show_spinner=False)
def query_clean(slug: str, sql: str, years: tuple[int, ...]):
    """Esegue SQL sul clean layer (cached 1h)."""
    return _query_clean(slug, sql, list(years), prefix=PREFIX)
