# Notes

## Tecnico

### Fonte
- URL pattern: `https://dati.consip.it/download/dataset/ordini-convenzione-{year}.csv`
- 16 colonne, latin-1
- ~11.3K righe nel 2026

### Anomalie note
- Encoding latin-1 (non utf-8)
- Alcune colonne numeriche hanno virgola come separatore decimale
- `Importo_Ordinato` può essere null (ordini senza importo)
- Prima colonna con `#` (`#Anno_Riferimento`)

## Analitico

### Domanda guida
Spesa reale della PA per convenzione.

### Metriche
- Importo totale per convenzione
- Numero ordini per convenzione
- Numero PA coinvolte
- Numero lotti e CPV distinti
