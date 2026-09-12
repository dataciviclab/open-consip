-- mart_analisi_mercato.sql — Analisi aggregata del mercato CONSIP vs ANAC
-- 1 riga per regione con metriche comparative.

SELECT
    regione_sede AS regione,
    COUNT(*) AS n_imprese,
    SUM(CASE WHEN profilo = 'dual_use' THEN 1 ELSE 0 END) AS imprese_dual_use,
    SUM(CASE WHEN profilo = 'solo_consip' THEN 1 ELSE 0 END) AS imprese_solo_consip,
    SUM(CASE WHEN profilo = 'solo_anac' THEN 1 ELSE 0 END) AS imprese_solo_anac,
    -- Metriche CONSIP
    SUM(agg_consip) AS totale_agg_consip,
    SUM(contratti_attivi_consip) AS totale_contratti_consip,
    -- Metriche ANAC
    SUM(agg_anac) AS totale_agg_anac,
    SUM(totale_attivita_anac) AS totale_attivita_anac,
    -- Medie
    ROUND(AVG(agg_consip), 1) AS media_agg_consip,
    ROUND(AVG(agg_anac), 1) AS media_agg_anac,
    -- Percentuale dual-use
    ROUND(SUM(CASE WHEN profilo = 'dual_use' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS pct_dual_use
FROM clean_input
WHERE regione_sede IS NOT NULL
GROUP BY regione_sede
HAVING COUNT(*) >= 10
ORDER BY n_imprese DESC
