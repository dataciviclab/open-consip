# Dizionario dati

## Consumi Convenzione (`consip-consumi-convenzione`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `regione` | TEXT | Regione italiana |
| `provincia` | TEXT | Provincia (sigla) |
| `convenzione` | TEXT | Nome convenzione |
| `tipologia_servizio` | TEXT | Tipo servizio (energia, gas, etc.) |
| `n_comuni` | INT | Numero comuni aderenti |
| `n_clienti` | INT | Numero clienti |
| `importo` | DOUBLE | Importo speso (€) |

## Bandi e Gare (`consip-bandie-gare`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di pubblicazione |
| `identificativo_lotto` | TEXT | Identificativo lotto CONSIP |
| `oggetto` | TEXT | Oggetto della gara |
| `tipologia` | TEXT | Tipo strumento (Convenzione, AQ, MePA) |
| `stato` | TEXT | Stato della gara |
| `data pubblicazione` | DATE | Data di pubblicazione |

## Operatori Economici (`consip-operatori-economici`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `partita_iva` | TEXT | Partita IVA dell'impresa |
| `denominazione` | TEXT | Nome dell'impresa |
| `regione_sede` | TEXT | Regione della sede legale |
| `provincia_sede` | TEXT | Provincia della sede legale |
| `forma_giuridica` | TEXT | Forma giuridica |

## Gare ASP (`consip-gare-asp`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `identificativo_lotto` | TEXT | Identificativo lotto CONSIP |
| `regione` | TEXT | Regione |
| `provincia` | TEXT | Provincia |
| `comune` | TEXT | Comune |
| `latitude` | DOUBLE | Latitudine |
| `longitude` | DOUBLE | Longitudine |

## Amministrazioni (`consip-amministrazioni`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `denominazione` | TEXT | Nome della PA |
| `regione` | TEXT | Regione |
| `provincia` | TEXT | Provincia |
| `latitude` | DOUBLE | Latitudine |
| `longitude` | DOUBLE | Longitudine |

## Partecipazioni (`consip-partecipazioni`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `identificativo_lotto` | TEXT | Identificativo lotto CONSIP |
| `partita_iva` | TEXT | Partita IVA dell'impresa |
| `denominazione` | TEXT | Nome dell'impresa |

## RDO/TD Stipulate (`consip-rdo-td-stipulate`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `identificativo_lotto` | TEXT | Identificativo lotto CONSIP |
| `oggetto` | TEXT | Oggetto della RDO/TD |
| `esito` | TEXT | Esito della procedura |

## Ordini Convenzione (`consip-ordini-convenzione`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `regione` | TEXT | Regione |
| `provincia` | TEXT | Provincia |
| `convenzione` | TEXT | Nome convenzione |
| `importo` | DOUBLE | Importo ordine (€) |

## Ordini MePA (`consip-ordini-mepa`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `regione` | TEXT | Regione |
| `provincia` | TEXT | Provincia |
| `bene_servizio` | TEXT | Tipo bene/servizio |
| `importo` | DOUBLE | Importo ordine (€) |

## Cataloghi (`consip-cataloghi`)

| Colonna | Tipo | Descrizione |
|---|---|---|
| `anno` | INT | Anno di riferimento |
| `codice_cpv` | TEXT | Codice CPV |
| `descrizione_cpv` | TEXT | Descrizione CPV |
| `categoria` | TEXT | Categoria bene/servizio |
| `n_cataloghi` | INT | Numero cataloghi attivi |
