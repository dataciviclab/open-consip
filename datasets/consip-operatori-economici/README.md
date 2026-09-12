# Consip — Operatori Economici del Programma

## Domanda guida

**Quante imprese partecipano attivamente al mercato Consip e dove sono concentrate?**
La distribuzione geografica delle imprese con contratti attivi Consip rispecchia la struttura produttiva italiana o rivela concentrazioni inusuali?

## Fonte

- **Ente**: Consip SpA / MEF
- **Portale**: [dati.consip.it](https://dati.consip.it)
- **Dataset**: OPERATORI ECONOMICI DEL PROGRAMMA
- **Formato**: CSV, delimitato `,`, encoding utf-8
- **Anni disponibili**: 2024, 2025, 2026
- **Aggiornamento**: annuale (file nominato per anno di edizione)
- **Licenza**: CC-BY-4.0

## Perimetro

- **Periodo**: 2024-2026 (3 anni)
- **Granularità**: impresa (una riga = un'impresa con attività su acquistinretepa.it)
- **Chiavi**: partita IVA, regione sede legale, forma societaria
- **Cosa contiene**: anagrafica imprese partecipanti al Programma Consip con sede legale, aggiudicazioni, abilitazioni, transazioni, contratti attivi

## Output minimo atteso

- `clean_input`: 14 colonne normalizzate, schema stabile cross-year
- `mart_imprese_per_territorio`: aggregazione per regione + forma societaria

## Boundary clean/mart

- **Clean**: rename colonne, cast tipi, normalizzazione stringhe. Nessuna aggregazione.
- **Mart**: conteggio imprese, somma aggiudicazioni/contratti per dimensione geografica.

## Criterio di promozione

- Pipeline completa su 2024-2026 (RAW → CLEAN → MART)
- Mart con almeno 5 righe per anno
- Nessun errore di validazione
- Analisi pubblicata che risponde alla domanda guida

## Stato

- **Pipeline**: in test
- **Validazione**: da verificare

## Prossimo passo

Run: `toolkit run -c datasets/consip-operatori-economici/dataset.yml --years 2024`
