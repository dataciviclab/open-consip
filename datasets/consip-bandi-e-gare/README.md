# Consip — Bandi e Gare del Programma

## Domanda guida

**Quanto passa da Consip (convenzioni, accordi quadro, MePA) vs gara diretta per settore/regione?**
La distribuzione dei bandi Consip per tipo di strumento (convenzione, AQ, MePA, SDAPA) e regione rivela differenze strutturali nell'uso degli strumenti di e-procurement pubblico?

## Fonte

- **Ente**: Consip SpA / MEF
- **Portale**: [dati.consip.it](https://dati.consip.it)
- **Dataset**: BANDI E GARE DEL PROGRAMMA
- **Formato**: CSV, delimitato `,`, encoding latin-1
- **Anni disponibili**: 2024, 2025, 2026
- **Aggiornamento**: annuale (file nominato per anno di edizione)
- **Licenza**: CC-BY-4.0

## Perimetro

- **Periodo**: 2024-2026 (3 anni)
- **Granularità**: lotto per bando (una riga = un lotto di un bando Consip)
- **Chiavi**: identificativo lotto, tipo strumento, criterio aggiudicazione
- **Cosa contiene**: bandi e gare pubblicati su acquistinretepa.it, con importi, criteri, operatori

## Output minimo atteso

- `clean_input`: 24 colonne normalizzate, schema stabile cross-year
- `mart_bandi_per_strumento`: aggregazione per tipo strumento + criterio aggiudicazione

## Boundary clean/mart

- **Clean**: rename colonne, cast tipi, parsing date italiane. Nessuna aggregazione.
- **Mart**: conteggio lotti, somma base asta, media erosione per dimensione analitica.

## Criterio di promozione

- Pipeline completa su 2024-2026 (RAW → CLEAN → MART)
- Mart con almeno 5 righe per anno
- Nessun errore di validazione
- Analisi pubblicata che risponde alla domanda guida

## Stato

- **Pipeline**: in test
- **Validazione**: da verificare

## Prossimo passo

Run: `toolkit run -c datasets/consip-bandi-e-gare/dataset.yml --years 2024`
