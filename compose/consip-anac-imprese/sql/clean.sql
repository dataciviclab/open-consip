-- clean.sql — Compose CONSIP+ANAC: profilo impresa dual-use
-- Unisce operatori economici CONSIP con mart_imprese ANAC su P.IVA/CF.
-- Output: 1 riga per impresa con attributi da entrambi i mercati.

WITH
consip AS (
    SELECT
        partita_iva,
        MAX(ragione_sociale) AS ragione_sociale_consip,
        MAX(forma_societaria) AS forma_societaria,
        MAX(regione_sede_legale) AS regione_sede,
        MAX(provincia_sede_legale) AS provincia_sede,
        MAX(comune_sede_legale) AS comune_sede,
        MAX(latitudine_sede_legale) AS latitudine,
        MAX(longitudine_sede_legale) AS longitudine,
        SUM(numero_aggiudicazioni) AS agg_consip,
        SUM(numero_abilitazioni) AS abilitazioni_consip,
        SUM(numero_transazioni) AS transazioni_consip,
        SUM(numero_contratti_attivi) AS contratti_attivi_consip
    FROM raw_input
    WHERE partita_iva IS NOT NULL AND TRIM(partita_iva) != ''
    GROUP BY partita_iva
),

anac AS (
    SELECT
        cf,
        MAX(denominazione) AS denominazione_anac,
        MAX(tipo_soggetto) AS tipo_soggetto,
        SUM(n_aggiudicazioni) AS agg_anac,
        SUM(n_gare_partecipate) AS partecipazioni_anac,
        SUM(n_subappalti) AS subappalti_anac,
        MAX(ruolo_prevalente) AS ruolo_prevalente,
        MAX(totale_attivita) AS totale_attivita_anac
    FROM read_parquet('/home/gabry/dev/dataciviclab-workspace/appalti-pubblici/out/data/mart/anac_cross/*/mart_imprese.parquet')
    WHERE cf IS NOT NULL AND TRIM(cf) != ''
    GROUP BY cf
),

tutti AS (
    -- Imprese presenti in entrambi i mercati
    SELECT
        c.partita_iva,
        COALESCE(c.ragione_sociale_consip, a.denominazione_anac) AS denominazione,
        c.forma_societaria,
        c.regione_sede,
        c.provincia_sede,
        c.comune_sede,
        c.latitudine,
        c.longitudine,
        -- Consip
        c.agg_consip,
        c.abilitazioni_consip,
        c.transazioni_consip,
        c.contratti_attivi_consip,
        -- Anac
        a.agg_anac,
        a.partecipazioni_anac,
        a.subappalti_anac,
        a.ruolo_prevalente,
        a.totale_attivita_anac,
        -- Flag dual-use
        1 AS ha_consip,
        1 AS ha_anac,
        'dual_use' AS profilo
    FROM consip c
    JOIN anac a ON c.partita_iva = a.cf

    UNION ALL

    -- Solo CONSIP
    SELECT
        c.partita_iva,
        c.ragione_sociale_consip AS denominazione,
        c.forma_societaria,
        c.regione_sede,
        c.provincia_sede,
        c.comune_sede,
        c.latitudine,
        c.longitudine,
        c.agg_consip,
        c.abilitazioni_consip,
        c.transazioni_consip,
        c.contratti_attivi_consip,
        0 AS agg_anac,
        0 AS partecipazioni_anac,
        0 AS subappalti_anac,
        NULL AS ruolo_prevalente,
        0 AS totale_attivita_anac,
        1 AS ha_consip,
        0 AS ha_anac,
        'solo_consip' AS profilo
    FROM consip c
    WHERE c.partita_iva NOT IN (SELECT cf FROM anac)

    UNION ALL

    -- Solo ANAC
    SELECT
        a.cf AS partita_iva,
        a.denominazione_anac AS denominazione,
        a.tipo_soggetto AS forma_societaria,
        NULL AS regione_sede,
        NULL AS provincia_sede,
        NULL AS comune_sede,
        NULL AS latitudine,
        NULL AS longitudine,
        0 AS agg_consip,
        0 AS abilitazioni_consip,
        0 AS transazioni_consip,
        0 AS contratti_attivi_consip,
        a.agg_anac,
        a.partecipazioni_anac,
        a.subappalti_anac,
        a.ruolo_prevalente,
        a.totale_attivita_anac,
        0 AS ha_consip,
        1 AS ha_anac,
        'solo_anac' AS profilo
    FROM anac a
    WHERE a.cf NOT IN (SELECT partita_iva FROM consip)
)

SELECT * FROM tutti
