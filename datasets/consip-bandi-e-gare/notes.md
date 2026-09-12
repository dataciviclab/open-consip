# Notes

## Tecnico

### Fonte
- Portale CKAN: `https://dati.consip.it`
- Dataset CKAN: `dataset-bandi-e-gare`
- URL pattern: `https://dati.consip.it/download/dataset/bandiegare{year}.csv`

### File CSV
- 29 colonne, header con `#` nella prima colonna (`#Denominazione_Bando`)
- Delimitatore: `,`
- Encoding: latin-1 ( NON utf-8 )
- Decimali: virgola (es. `3841,24`)
- Schema identico per tutti gli anni

### Anomalie note
- La prima colonna inizia con `#`, va quotata in SQL come `"#Denominazione_Bando"`
- I valori numerici con virgola decimale sono stringhe
- Le date non sono ISO (formato italiano)
- `Base_Asta` e `Importo_Massimale` sono stringhe con separatori italiani

## Analitico

### Domanda guida
Distribuzione dei bandi Consip per tipo di strumento e regione.

### Dimensioni analitiche
- Temporale: anno
- Strumento: Convenzione, AQ, MePA, SDAPA
- Geografica: regione (non nel dataset, ma agganciabile)
- Procedura: tipo procedura, criterio aggiudicazione

### Metriche
- Numero lotti
- Base asta totale
- Erosione media
- Numero operatori medi

## Cautele

- La serie storica è omogenea? Sì, schema identico per 2024-2026
- Ci sono discontinuità dichiarate? Non dichiarate
- I valori nulli sono zero reale o dato mancante? Da verificare
- `Base_Asta` potrebbe avere null (bandi senza importo)
- **Deroga primary_key**: `identificativo_lotto` NON è unico — lo stesso lotto compare in più bandi (58 duplicati su 1823 righe nel 2024). Il lotto è identificativo di specializzazione merceologica, non di gara. Per unicità servirebbe `(identificativo_lotto, denominazione_bando)` o simile, ma la granularità reale del dataset è lotto × bando.
