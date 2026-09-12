# Consip — RDO/TD Stipulate MePA

## Domanda quida

**Quanto tempo ci mette la PA a firmare contratti su MePA e con quanti fornitori?**
Le metriche di competizione (tempo di stipula, fornitori medi, % base asta valorizzata) variano tra regioni e tipi di negoziazione?

## Fonte

- **Ente**: Consip SpA / MEF
- **Dataset**: RDO/TD STIPULATE SUL MEPA
- **Formato**: CSV, utf-8
- **Anni disponibili**: 2024, 2025, 2026
- **Licenza**: CC-BY-4.0

## Perimetro

- **Granularità**: regione × tipo negoziazione × anno
- **Chiavi**: regione_pa, tipo_negoziazione
- **Cosa contiene**: contratti stipulati via RDO/TD su MePA con valori, fornitori, tempi di stipula

## Metriche chiave

- `Perc_negoziazioni_base_asta_valorizzata` = % RDO con base asta valorizzata (proxy competizione)
- `Tempi_Medi_Stipula` = giorni medi tra pubblicazione e stipula
- `Durata_media_negoziazione` = durata media della negoziazione
- `N_Medio_Fornitori_Partecipanti` = fornitori medi per negoziazione

## Join

- `amministrazioni` su (regione_pa)
- `bandi-e-gare` su (tipo_strumento = 'MePA')

## Stato

- **Pipeline**: in test
