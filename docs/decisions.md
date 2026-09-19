# Decisioni progettuali

## ADR-001: Modello multi-dataset

**Stato**: accettata
**Contesto**: il repo open-consip raccoglie 10+ dataset dalla stessa fonte (dati.consip.it), ciascuno con schema e logica diversa.

**Decisione**: un dataset = una dir in `datasets/` con il proprio `dataset.yml`. Condividere `support/` per anagrafiche usate da più dataset. Nessun `dataset.yml` root.

**Conseguenze**: il Makefile e il CI scansionano `datasets/` e `support/` automaticamente. Ogni dataset è indipendente ma può dipendere da support.

## Ordini: limitazione strutturale

Le colonne `n_ordini` e `importo` nei dataset ordini non sono mai entrambe presenti. Questa è una limitazione della fonte CONSIP, non un bug della pipeline.

## identificativo_lotto ≠ CIG

`identificativo_lotto` nei dati CONSIP è un hash alfanumerico (10 hex chars). Il CIG di ANAC ha lo stesso formato ma è assegnato da ANAC e non corrisponde ai lotti CONSIP. L'unico incrocio possibile tra CONSIP e ANAC è sulle imprese (P.IVA/CF).

## Compose read_parquet

Il compose `consip-composto` usa `read_parquet` con glob pattern (`/*_clean.parquet`) per aggregare più anni. Il toolkit non supporta nativamente questo pattern: il compose dipende dalla struttura dei path di output del toolkit.

## Dashboard senzaoutput committati

La dashboard legge parquet da `out/data/mart/` che non vengono committati (`.gitignore`). La dashboard funziona solo dopo aver eseguito `make run`.
