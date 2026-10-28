# Consip — consumi in convenzione: geografia della spesa delle PA

## Domanda guida

**Le regioni del Sud Italia pagano di più per le utility in convenzione Consip rispetto al Nord?**
La spesa per energia, gas e carburanti delle PA italiane tramite Consip è omogenea territorialmente, o ci sono divari strutturali che persistono anno dopo anno?

## Fonte

- **Ente**: Consip SpA / MEF
- **Portale**: [dati.consip.it](https://dati.consip.it)
- **Dataset**: CONSUMI GENERATI TRAMITE ORDINI DIRETTI DI ACQUISTO IN CONVENZIONE
- **Formato**: CSV, delimitato `,`, encoding utf-8
- **Anni disponibili**: 2024, 2025, 2026
- **Aggiornamento**: annuale (file nominato per anno di edizione)
- **Licenza**: CC-BY-4.0

## Perimetro

- **Periodo**: 2024-2026 (3 anni)
- **Granularità**: lotto-convenzione-provincia-PA (una riga = consumo aggregato per coppia PA-convenzione-lotto)
- **Chiavi territoriali**: regione PA, provincia PA, sigla provincia, regione fornitore
- **Cosa contiene**: consumi economici di energia e utility (elettricità, gas, carburanti) acquistati tramite ordini diretti in convenzione Consip

## Output minimo atteso

- `clean_input`: 12 colonne normalizzate, schema stabile cross-year
- `mart_consumi_convenzione`: aggregazione geografica per anno, regione, provincia, tipologia PA

## Boundary clean/mart

- **Clean**: rename colonne, cast tipi, conversione virgola→punto per decimali. Nessuna aggregazione.
- **Mart**: somma valore consumi, conteggio ordini/PA/PO per dimensione geografica. Nessun join esterno.

## Schema

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno_riferimento` | INTEGER | Anno di riferimento del consumo |
| `tipologia_amministrazione` | VARCHAR | Tipologia PA (Comune, Università, ASL, etc.) |
| `regione_pa` | VARCHAR | Regione della PA acquirente |
| `provincia_pa` | VARCHAR | Provincia della PA acquirente |
| `sigla_provincia_pa` | VARCHAR | Sigla provincia (2 char) |
| `regione_fornitore` | VARCHAR | Regione del fornitore |
| `convenzione` | VARCHAR | Nome convenzione Consip |
| `lotto` | VARCHAR | Lotto della convenzione |
| `valore_economico_consumi` | DOUBLE | Valore economico consumi (€) |
| `numero_ordini_con_consumi` | BIGINT | Numero ordini con consumi |
| `n_pa_con_consumi` | BIGINT | Numero PA con consumi |
| `n_po_con_consumi` | BIGINT | Numero punti di prelievo con consumi |

## Rischi noti

- **Sede fornitore ≠ luogo esecuzione**: la regione del fornitore non coincide necessariamente con il luogo dove il servizio viene erogato
- **Non copre tutte le categorie merceologiche Consip**: solo utility (energia, gas, carburanti)
- **Serie storica breve**: 3 anni (2024-2026), insufficiente per trend strutturali
- **Dati aggregati, non additivi**: i valori sono aggregate statistiche, non transazioni singole
- **Il 2023 non è più pubblicato dalla fonte**: Consip tiene una finestra mobile di 3 anni; il file `consumi-in-convenzione-2023.csv` risponde 404 e il 2026 lo ha sostituito. La serie 2023 esiste **solo nel nostro snapshot** (clean pubblicato) e **non è più riproducibile**: va trattata come dato storico non rigenerabile.
- **Il file 2026 era un duplicato fino a fine 2025**: era copia del 2025 (dato non ancora aggiornato) — motivo per cui il dataset era fermo a `2023-2025`. Verificato il 2026-10-28: il file è ora distinto (1,05 MB il 2025, 0,91 MB il 2026), quindi entra nel perimetro.

## Criterio di promozione

- Pipeline completa su 2024-2026 (RAW → CLEAN → MART)
- Mart con almeno 10 righe per anno
- Nessun errore di validazione su `not_null` e `primary_key`
- Analisi pubblicata che risponde alla domanda guida

## Stato

- **Pipeline**: ✅ funzionante (RAW → CLEAN → MART)
- **Validazione**: ✅ passata su tutti gli anni
- **Output**: `mart_spesa_per_territorio` (8048 righe/anno)
- **Readiness**: needs-review (7/8)

## Prossimo passo

Run completo: `make run`
