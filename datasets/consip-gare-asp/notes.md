# Notes

## Tecnico

### Fonte
- Portale CKAN: `https://dati.consip.it`
- Dataset CKAN: `dataset-gare-asp`
- URL pattern: `https://dati.consip.it/download/dataset/gareasp{year}.csv`

### File CSV
- 25 colonne, header con `#` nella prima colonna (`#Anno_Riferimento`)
- Delimitatore: `,`
- Encoding: latin-1 ( NON utf-8 )
- Schema identico per tutti gli anni

### Anomalie note
- La prima colonna inizia con `#`, va quotata in SQL come `"#Anno_Riferimento"`
- `Base_asta` e `Valore_aggiudicato` sono stringhe con separatori italiani
- Le date non sono ISO (formato italiano)
- Le coordinate geografiche (`Latitudine_PA`, `Longitudine_PA`) sono la chiave unica del dataset
- `Stato_gara` ha valori testuali non standardizzati

## Analitico

### Domanda guida
Distribuzione geografica delle gare ASP Consip.

### Dimensioni analitiche
- Temporale: anno
- Geografica: regione, provincia, coordinate PA
- Stato: stato gara, stato lotto
- Procedura: tipo procedura, criterio aggiudicazione

### Metriche
- Numero gare
- Base asta totale
- Valore aggiudicato totale
- Numero fornitori medio

## Cautele

- La serie storica è omogenea? NO — 2024/2025 hanno 39 colonne nel raw, 2026 ne ha 25. Il clean.sql mappa solo le 25 colonne comuni, le extra vengono ignorate.
- Ci sono discontinuità dichiarate? Non dichiarate
- I valori nulli sono zero reale o dato mancante? `Denominazione_amministrazione` ha 1 null su ~6700 righe
- **Deroga primary_key**: `identificativo_lotto` NON è unico (155 duplicati su 6700 righe). Lo stesso lotto compare in più gare/PA. Stessa logica di bandi-e-gare.
- `Base_asta` e `Valore_aggiudicato` potrebbero avere null (gare senza importo o senza aggiudicazione)
