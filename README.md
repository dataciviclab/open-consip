# Open CONSIP — DataCivicLab

**Come la PA italiana acquista beni e servizi via Consip, e con quali differenze territoriali?**

Sistema di intelligence sugli acquisti CONSIP: raccoglie i dati open data (dati.consip.it),
li trasforma in mart analitici e li rende interrogabili via dashboard Streamlit.

- **Fonte**: [CONSIP Open Data](https://dati.consip.it/)
- **Copertura**: 2023-2026, Italia
- **Unità di analisi**: Regione / Provincia / Impresa
- **Output pubblico**: Dashboard Streamlit + Discussion

## Cosa risponde

1. **Quanto passa da CONSIP per settore e regione?** → spesa per convenzioni, accordi quadro, MePA
2. **Quali imprese dominano il mercato?** → concentrazione, ruolo, dual-use CONSIP+ANAC
3. **Le gare ASP sono concentrate nelle grandi città?** → distribuzione territoriale con geo
4. **Quale competizione nelle procedure?** → numero offerenti, criteri, esiti
5. **I prodotti sono disponibili?** → cataloghi con codici CPV
6. **Le regioni del Sud pagano di più per le utility?** → spesa convenzione per territorio

## Dataset

| Dataset | Cosa contiene | Anni | Mart |
|---|---|---|---|
| `consip-consumi-convenzione` | Spesa utility PA per convenzione | 2023-2025 | 1 |
| `consip-bandie-gare` | Bandi e gare del Programma | 2024-2026 | 2 |
| `consip-operatorieconomici` | Anagrafica imprese con attività CONSIP | 2024-2026 | 2 |
| `consip-gareasp` | Gare ASP geolocalizzate | 2024-2026 | 2 |
| `consip-ordiniconvenzione` | Ordini diretti in convenzione | 2024-2026 | 1 |
| `consip-ordinimpepa` | Ordini su MePA per bene/servizio | 2024-2026 | 2 |
| `consip-partecipazioni` | Imprese partecipanti alle iniziative | 2024-2026 | 1 |
| `consip-rdotdstipulate` | Richieste di offerta/trattative dirette | 2024-2026 | 1 |
| `consip-amministrazioni` | Anagrafica PA con coordinate | 2024-2026 | 1 |
| `consip-cataloghi` | Catalogo beni/servizi disponibili | 2024-2026 | 1 |

### Mart analitici (14 dataset + 2 compose)

**Spesa** (2): mart_spesa_per_territorio, mart_spesa_per_convenzione

**Gare** (4): mart_bandi_per_strumento, mart_competizione_strumento, mart_gare_per_territorio, mart_esito_gare_provincia

**Imprese** (2): mart_imprese_per_territorio, mart_concentrazione_imprese

**Imprese dual-use** (2): mart_imprese_per_territorio, mart_concentrazione_imprese (compose CONSIP+ANAC)

**Altri** (4): mart_pa_per_territorio, mart_vincitori_per_strumento, mart_competizione_mepa, mart_cataloghi_per_categoria

**Ordini MePA** (2): mart_ordini_mepa_per_bene, mart_ordini_mepa_per_regione

## Compose CONSIP+ANAC

Il compose `consip-anac-imprese` unisce operatori economici CONSIP con aggiudicatari ANAC
su P.IVA/CF per identificare le imprese "dual-use" attive in entrambi i mercati.

| Compose | Cosa | Mart |
|---|---|---|
| `compose/consip-anac-imprese` | Profilo impresa dual-use CONSIP+ANAC | 2 |

### Key insight

- **174K imprese dual-use** (24.5%) attive in entrambi i mercati
- **139K solo CONSIP** (19.6%)
- **397K solo ANAC** (55.8%)
- Lombardia: 66.8% dual-use (la più integrata)

## Dashboard

Dashboard Streamlit con 7 pagine:

| Pagina | Contenuto |
|---|---|
| Panoramica | KPI generali, trend spesa |
| Spesa per Strumento | Convenzioni, AQ, MePA per territorio |
| Mercato PA | Imprese dual-use CONSIP vs ANAC |
| Competizione MePA | Analisi competizione RDO/TD |
| Imprese | Profilo imprese, concentrazione |
| Cataloghi | Prodotti disponibili con CPV |
| Query SQL | Query libera su tutti i dataset |

## Come si usa

```bash
# Setup
pip install -r requirements.txt

# Validare config
make check

# Eseguire support dataset
make seeds

# Eseguire tutte le pipeline
make run

# Dashboard
cd dashboard && streamlit run app.py

# Test
python -m pytest tests/
```

## Struttura

```
open-consip/
├── datasets/                   # 10 dataset singoli (toolkit pipeline)
│   ├── consip-amministrazioni/
│   ├── consip-bandie-gare/
│   ├── consip-cataloghi/
│   ├── consip-consumi-convenzione/
│   ├── consip-gare-asp/
│   ├── consip-operatorieconomici/
│   ├── consip-ordini-convenzione/
│   ├── consip-ordini-mepa/
│   ├── consip-partecipazioni/
│   └── consip-rdo-td-stipulate/
├── compose/
│   └── consip-anac-imprese/    # cross-consip-anac (dual-use)
├── dashboard/                  # Streamlit (7 pagine)
│   └── pages/
├── docs/                       # sources, decisions, data_dictionary
├── tests/                      # contract test
├── .github/workflows/          # check.yml, pipeline.yml
├── Makefile
└── requirements.txt
```

## CI/CD

- **check.yml**: Valida i config YAML e audita i test marker su ogni PR/push (reusable workflows)
- **pipeline.yml**: Esegue le pipeline mensilmente o su manuale (reusable workflow)

## Perché fidarsi

- Fonti ufficiali CONSIP (`dati.consip.it`)
- Trasformazioni documentate in SQL
- Controlli automatici prima della pubblicazione (CI + contract test)
- Standard condivisi del DataCivicLab (`.github`)

## Partecipa

- **Discussions** → domande civiche, interpretazioni, proposte di metriche
- **Issues** → bug, problemi tecnici, miglioramenti della pipeline

## Confine con il toolkit

Il motore della pipeline vive nel repository `toolkit`. Questa repo non replica
la logica di esecuzione: definisce input, regole e output attesi per ogni dataset.

- bug o feature di CLI, runner, validazioni runtime → repo `toolkit`
- bug o modifiche a fonti, mapping, SQL, mart, docs → questa repo

## Licenza

- **Dati CONSIP**: CC BY 4.0
- **Codice**: MIT
