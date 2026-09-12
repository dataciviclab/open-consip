-- clean.sql — CONSIP Compose: snapshot unificato anno × regione
-- Unisce tutti i dataset Consip a livello di anno × regione.
-- Output: 1 riga per anno × regione con tutti gli attributi cross-dataset.
-- USA read_parquet con glob per leggere TUTTI gli anni dei support.

WITH

-- ── 1. GARE ASP: metriche gare per anno × regione ──
gare_asp AS (
    SELECT
        anno_riferimento AS anno,
        regione_pa AS regione,
        count(*) AS n_gare,
        sum(case when stato_gara = 'Gara aggiudicata definitivamente' then 1 else 0 end) AS n_aggiudicate,
        round(sum(case when stato_gara = 'Gara aggiudicata definitivamente' then 1.0 else 0 end) * 100 / count(*), 1) AS tasso_aggiudicazione,
        sum(base_asta) AS base_asta_totale,
        sum(valore_aggiudicato) AS valore_aggiudicato_totale,
        round(sum(valore_aggiudicato) / nullif(sum(base_asta), 0) * 100, 1) AS incidenza_prezzo,
        avg(numero_fornitori_partecipanti) AS fornitori_medi_asp
    FROM raw_input
    GROUP BY anno_riferimento, regione_pa
),

-- ── 2. RDO-TD STIPULATE: competizione MePA (tutti gli anni) ──
rdo_td AS (
    SELECT
        anno_riferimento AS anno,
        regione_pa AS regione,
        sum(n_contratti_stipulati) AS n_contratti_mepa,
        sum(valore_contratti_stipulati) AS valore_contratti_mepa,
        avg(n_medio_fornitori_partecipanti) AS fornitori_medi_mepa,
        avg(tempi_medi_stipula) AS tempi_medi_stipula
    FROM read_parquet('{root}/data/clean/consip_rdo_td_stipulate/*/*_clean.parquet', hive_partitioning=false)
    GROUP BY anno_riferimento, regione_pa
),

-- ── 3. OPERATORI ECONOMICI: imprese per regione (tutti gli anni) ──
operatori AS (
    SELECT
        anno_riferimento AS anno,
        regione_sede_legale AS regione,
        count(*) AS n_imprese_totali,
        sum(case when numero_aggiudicazioni > 0 then 1 else 0 end) AS n_imprese_con_agg,
        sum(case when numero_contratti_attivi > 0 then 1 else 0 end) AS n_imprese_con_contratti,
        sum(numero_aggiudicazioni) AS tot_aggiudicazioni
    FROM read_parquet('{root}/data/clean/consip_operatori_economici/*/*_clean.parquet', hive_partitioning=false)
    GROUP BY anno_riferimento, regione_sede_legale
),

-- ── 4. CONSUMI CONVENZIONE: spesa utility (tutti gli anni) ──
consumi AS (
    SELECT
        anno_riferimento AS anno,
        regione_pa AS regione,
        sum(valore_economico_consumi) AS spesa_utility,
        sum(numero_ordini_con_consumi) AS ordini_utility
    FROM read_parquet('{root}/data/clean/consip_consumi_convenzione/*/*_clean.parquet', hive_partitioning=false)
    GROUP BY anno_riferimento, regione_pa
),

-- ── 5. ORDINI CONVENZIONE: spesa totale (tutti gli anni) ──
ordini AS (
    SELECT
        anno_riferimento AS anno,
        regione_pa AS regione,
        sum(importo_ordinato) AS spesa_ordini,
        sum(n_ordini) AS n_ordini_totali,
        sum(n_pa) AS n_pa_con_ordini
    FROM read_parquet('{root}/data/clean/consip_ordini_convenzione/*/*_clean.parquet', hive_partitioning=false)
    WHERE importo_ordinato > 0
    GROUP BY anno_riferimento, regione_pa
),

-- ── 6. AMMINISTRAZIONI: anagrafica PA (tutti gli anni) ──
amministrazioni AS (
    SELECT
        anno_riferimento AS anno,
        regione,
        count(*) AS n_pa_totali,
        sum(numero_po_attivi) AS n_po_totali
    FROM read_parquet('{root}/data/clean/consip_amministrazioni/*/*_clean.parquet', hive_partitioning=false)
    GROUP BY anno_riferimento, regione
),

-- ── UNIONE: tutti i CIG unici da tutte le sorgenti ──
tutti_anno_regione AS (
    SELECT anno, regione FROM gare_asp
    UNION
    SELECT anno, regione FROM rdo_td
    UNION
    SELECT anno, regione FROM operatori
    UNION
    SELECT anno, regione FROM consumi
    UNION
    SELECT anno, regione FROM ordini
    UNION
    SELECT anno, regione FROM amministrazioni
)

SELECT
    t.anno,
    t.regione,

    -- gare ASP
    COALESCE(g.n_gare, 0) AS n_gare,
    COALESCE(g.n_aggiudicate, 0) AS n_aggiudicate,
    g.tasso_aggiudicazione,
    COALESCE(g.base_asta_totale, 0) AS base_asta_totale,
    COALESCE(g.valore_aggiudicato_totale, 0) AS valore_aggiudicato_totale,
    g.incidenza_prezzo,
    g.fornitori_medi_asp,

    -- rdo TD stipulate
    COALESCE(r.n_contratti_mepa, 0) AS n_contratti_mepa,
    COALESCE(r.valore_contratti_mepa, 0) AS valore_contratti_mepa,
    r.fornitori_medi_mepa,
    r.tempi_medi_stipula,

    -- operatori economici
    COALESCE(o.n_imprese_totali, 0) AS n_imprese_totali,
    COALESCE(o.n_imprese_con_agg, 0) AS n_imprese_con_agg,
    COALESCE(o.n_imprese_con_contratti, 0) AS n_imprese_con_contratti,
    COALESCE(o.tot_aggiudicazioni, 0) AS tot_aggiudicazioni,

    -- consumi utility
    COALESCE(c.spesa_utility, 0) AS spesa_utility,
    COALESCE(c.ordini_utility, 0) AS ordini_utility,

    -- ordini totali
    COALESCE(e.spesa_ordini, 0) AS spesa_ordini,
    COALESCE(e.n_ordini_totali, 0) AS n_ordini_totali,
    COALESCE(e.n_pa_con_ordini, 0) AS n_pa_con_ordini,

    -- amministrazioni
    COALESCE(f.n_pa_totali, 0) AS n_pa_totali,
    COALESCE(f.n_po_totali, 0) AS n_po_totali

FROM tutti_anno_regione t
LEFT JOIN gare_asp g ON t.anno = g.anno AND t.regione = g.regione
LEFT JOIN rdo_td r ON t.anno = r.anno AND t.regione = r.regione
LEFT JOIN operatori o ON t.anno = o.anno AND t.regione = o.regione
LEFT JOIN consumi c ON t.anno = c.anno AND t.regione = c.regione
LEFT JOIN ordini e ON t.anno = e.anno AND t.regione = e.regione
LEFT JOIN amministrazioni f ON t.anno = f.anno AND t.regione = f.regione
ORDER BY t.anno, t.regione
