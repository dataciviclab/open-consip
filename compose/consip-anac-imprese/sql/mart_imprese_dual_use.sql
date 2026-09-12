-- mart_imprese_dual_use.sql — Imprese attive in entrambi i mercati (CONSIP + ANAC)
-- 1 riga per impresa con metriche da entrambi i lati.

SELECT
    partita_iva,
    denominazione,
    forma_societaria,
    regione_sede,
    provincia_sede,
    comune_sede,
    latitudine,
    longitudine,
    -- CONSIP
    agg_consip,
    abilitazioni_consip,
    transazioni_consip,
    contratti_attivi_consip,
    -- ANAC
    agg_anac,
    partecipazioni_anac,
    subappalti_anac,
    ruolo_prevalente,
    totale_attivita_anac,
    -- Metriche composite
    agg_consip + agg_anac AS totale_aggiudicazioni,
    profilo,
    -- Indice di diversificazione: bilancia attività CONSIP vs ANAC
    -- Usa abilitazioni+contratti come proxy CONSIP (le agg sono sempre 0)
    CASE 
        WHEN (abilitazioni_consip + contratti_attivi_consip) + totale_attivita_anac = 0 THEN 0
        ELSE ROUND(2.0 * LEAST(abilitazioni_consip + contratti_attivi_consip, totale_attivita_anac) 
              / ((abilitazioni_consip + contratti_attivi_consip) + totale_attivita_anac), 2)
    END AS indice_diversificazione
FROM clean_input
WHERE partita_iva IS NOT NULL
ORDER BY totale_aggiudicazioni DESC
