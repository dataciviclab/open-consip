# Notes

## Tecnico

### Fonte
- Portale CKAN: `https://dati.consip.it`
- Dataset CKAN: `dataset-amministrazioni`
- URL pattern: `https://dati.consip.it/download/dataset/amministrazioni{year}.csv`

### File CSV
- 11 colonne, header con `#` nella prima colonna (`#Identificativo_Amministrazione`)
- Encoding: utf-8
- Schema identico per tutti gli anni

### Anomalie note
- La prima colonna inizia con `#`, va quotata in SQL come `"#Identificativo_Amministrazione"`
- Alcune denominazioni hanno caratteri non standard (es. "1°" -> encoding misto)
- `Codice_Fiscale` potrebbe non essere unico (sed multiple della stessa PA)
- `Identificativo_IPA` è il codice IPA della PA (join universale)

## Analitico

### Domanda guida
Anagrafica delle PA attive su Consip.

### Dimensioni analitiche
- Geografica: regione, provincia, comune
- Tipologia: tipologia amministrazione
- Attività: numero PO attivi

### Metriche
- Numero PA per regione/tipologia
- Numero PO totali per regione
- Coordinate medie (per geo implicita)

## Cautele

- Il dataset è un'anagrafica, non una transazione
- `Numero_PO_attivi` è un conteggio al momento dello snapshot, non cumulativo
- Le PA con 0 PO attivi non sono nel dataset (filtro implicito)
