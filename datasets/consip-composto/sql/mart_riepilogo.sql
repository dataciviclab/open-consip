-- mart_riepilogo.sql — Vista riassuntiva per dashboard
-- Una riga per anno × regione con le metriche più importanti.

SELECT
    anno,
    regione,

    -- gare ASP
    n_gare,
    n_aggiudicate,
    tasso_aggiudicazione,
    base_asta_totale,
    valore_aggiudicato_totale,
    incidenza_prezzo,
    fornitori_medi_asp,

    -- competizione MePA
    n_contratti_mepa,
    valore_contratti_mepa,
    fornitori_medi_mepa,
    tempi_medi_stipula,

    -- imprese
    n_imprese_totali,
    n_imprese_con_agg,
    n_imprese_con_contratti,

    -- spesa
    spesa_utility,
    spesa_ordini,

    -- PA
    n_pa_totali,
    n_po_totali

FROM clean_input
ORDER BY anno, regione
