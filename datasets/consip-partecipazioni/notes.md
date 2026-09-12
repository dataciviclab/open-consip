# Notes

## Tecnico

### Fonte
- Portale CKAN: `https://dati.consip.it`
- URL pattern: `https://dati.consip.it/download/dataset/partecipazioni{year}.csv`

### File CSV
- 12 colonne, header con `#` nella prima colonna
- Encoding: utf-8
- **678K righe nel 2026** — il più grande dei dataset CONSIP

### Anomalie note
- `Data_Aggiudicazione/Abilitazione` ha `/` nel nome colonna — va quotata
- `Esito_Partecipazione` ha valori testuali (Aggiudicatario, Abilitato, ecc.)
- `Partita_Iva` potrebbe non essere unica (impresa con più partecipazioni)
- Il dataset è un'anagrafica di partecipazioni, non transazioni

## Analitico

### Domanda guida
Competizione e concentrazione nelle gare Consip.

### Metriche
- Numero partecipazioni per tipo strumento
- Numero imprese distinte per esito
- Numero lotti coinvolti

## Cautele

- Il dataset è molto grande (678K righe) — attenzione alle performance
- Non tutti gli anni hanno lo stesso numero di righe (crescente)
- Le partecipazioni con `esito = 'Non Aggiudicatario'` sono la maggioranza
