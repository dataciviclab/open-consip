# Fonti dati

## Fonti primarie

| Fonte | URL | Protocollo | Licenza | Copertura |
|---|---|---|---|---|
| CONSIP Open Data | `https://dati.consip.it` | CKAN | CC BY 4.0 | 2023-2026 |

### Dataset CONSIP

| Slug | Risorsa CKAN | Descrizione |
|---|---|---|
| `consip-consumi-convenzione` | `consumi_convenzione_YYYY.csv` | Spesa utility PA per convenzione |
| `consip-bandi-e-gare` | `bandi_e_gare_YYYY.csv` | Bandi e gare del Programma |
| `consip-operatori-economici` | `operatori_economici_YYYY.csv` | Anagrafica imprese con attività CONSIP |
| `consip-gare-asp` | `gare_asp_YYYY.csv` | Gare ASP geolocalizzate |
| `consip-amministrazioni` | `amministrazioni_YYYY.csv` | Anagrafica PA con coordinate |
| `consip-partecipazioni` | `partecipazioni_YYYY.csv` | Imprese partecipanti alle iniziative |
| `consip-rdo-td-stipulate` | `rdo_td_stipulate_YYYY.csv` | Richieste di offerta/trattative dirette |
| `consip-ordini-convenzione` | `ordini_convenzione_YYYY.csv` | Ordini diretti in convenzione |
| `consip-ordini-mepa` | `ordini_mepa_YYYY.csv` | Ordini effettuati su MePA per bene/servizio |
| `consip-cataloghi` | `cataloghi_YYYY.csv` | Catalogo beni/servizi disponibili su Consip |

## Fonti secondarie (compose)

| Compose | Fonti | Uso |
|---|---|---|
| `consip-anac-imprese` | CONSIP operatori-economici + ANAC mart_imprese | Profilo impresa dual-use CONSIP+ANAC |

## Note

- Tutti i file CONSIP sono in formato CSV, codifica UTF-8, separatore `;`
- I nomi file seguono il pattern `{nome_dataset}{YYYY}.csv`
- Le fonti non forniscono API con limiti pubblici noti; i dati sono scaricabili liberamente
- Le colonne `n_ordini` e `importo` nei dataset ordini non sono mai entrambe presenti (limitazione strutturale della fonte)
