# Consip — Gare ASP (Application Service Provider)

## Domanda guida

**Le gare ASP Consip sono concentrate nelle grandi città o si distribuiscono uniformemente sul territorio?**
La distribuzione geografica delle gare ASP (procedure telematiche gestite da Consip per conto delle PA) rivela patterns di utilizzo diversi tra Nord e Sud?

## Fonte

- **Ente**: Consip SpA / MEF
- **Portale**: [dati.consip.it](https://dati.consip.it)
- **Dataset**: GARE ASP
- **Formato**: CSV, delimitato `,`, encoding latin-1
- **Anni disponibili**: 2024, 2025, 2026
- **Aggiornamento**: annuale (file nominato per anno di edizione)
- **Licenza**: CC-BY-4.0

## Perimetro

- **Periodo**: 2024-2026 (3 anni)
- **Granularità**: lotto per gara (una riga = un lotto di una gara ASP)
- **Chiavi**: identificativo lotto, regione PA, stato gara
- **Cosa contiene**: gare bandite dalle PA che utilizzano il sistema ASP di Consip, con geolocalizzazione (lat/lon PA)

## Output minimo atteso

- `clean_input`: 25 colonne normalizzate, schema stabile cross-year
- `mart_gare_per_territorio`: aggregazione per regione + stato gara

## Boundary clean/mart

- **Clean**: rename colonne, cast tipi, parsing date italiane, normalizzazione valori. Nessuna aggregazione.
- **Mart**: conteggio gare, somma base asta/valore aggiudicato, media fornitori per dimensione geografica.

## Criterio di promozione

- Pipeline completa su 2024-2026 (RAW → CLEAN → MART)
- Mart con almeno 5 righe per anno
- Nessun errore di validazione
- Analisi pubblicata che risponde alla domanda guida

## Stato

- **Pipeline**: in test
- **Validazione**: da verificare

## Prossimo passo

Run: `toolkit run -c datasets/consip-gare-asp/dataset.yml --years 2024`
