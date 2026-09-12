# Notes

## Tecnico

### Fonte
- URL pattern: `https://dati.consip.it/download/dataset/rdo-td-stipulate-mepa-{year}.csv`
- 18 colonne, utf-8
- ~12.8K righe nel 2026

### Anomalie note
- Alcune colonne numeriche sono stringhe con virgola (normalize_italian_number)
- `Perc_negoziazioni_base_asta_valorizzata` può essere null (nessuna RDO con base asta)
- `Tempi_Medi_Stipula` e `Durata_media_negoziazione` in giorni

## Analitico

### Domanda guida
Efficienza e competizione nel MePA.

### Metriche
- Numero contratti per regione/tipo
- Valore contratti per regione
- Fornitori medi (proxy competizione)
- Tempi di stipula (proxy efficienza)
