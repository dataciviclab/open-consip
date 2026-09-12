# Notes

## Tecnico

### Fonte
- Portale CKAN: `https://dati.consip.it`
- Dataset CKAN: `dataset-operatori-economici`
- URL pattern: `https://dati.consip.it/download/dataset/operatori_economici{year}.csv`

### File CSV
- 14 colonne, header con `#` nella prima colonna (`#Partita_Iva`)
- Delimitatore: `,`
- Encoding: utf-8
- Schema identico per tutti gli anni

### Anomalie note
- La prima colonna inizia con `#`, va quotata in SQL come `"#Partita_Iva"`
- `Partita_Iva` potrebbe non essere unica (impresa con più sedi)
- Le coordinate geografiche potrebbero avere null per imprese senza geo
- `Forma_Societaria` ha valori testuali non standardizzati

## Analitico

### Domanda guida
Distribuzione geografica delle imprese con attività Consip.

### Dimensioni analitiche
- Temporale: anno
- Geografica: regione, provincia, comune sede legale
- Tipo: forma societaria

### Metriche
- Numero imprese
- Numero aggiudicazioni totali
- Numero contratti attivi totali
- Coordinate medie (per geo implicita)

## Cautele

- La serie storica è omogenea? Sì, schema identico per 2024-2026
- Ci sono discontinuità dichiarate? Non dichiarate
- **`Partita_Iva` ha 652 null su ~6000 righe** (2024): sono imprese senza P.IVA nel dataset. Non è un errore, ma va considerato nei join con ANAC (dove la P.IVA è il campione primario).
- Le imprese con `numero_aggiudicazioni = 0` sono abilitate ma mai aggiudicate
- Il dataset è un'anagrafica, non una transazione: le colonne numeriche sono totali cumulative, non annuali
