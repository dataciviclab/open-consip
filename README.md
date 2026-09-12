# Consip — DataCivicLab

Questo repository raccoglie **dataset su Consip / e-procurement pubblico** per rispondere a
domande civiche: **come la PA italiana acquista beni e servizi, e con quali differenze territoriali?**

È un repo **multi-dataset**: ogni dataset vive in `datasets/<slug>/`, le
anagrafiche condivise in `support/`. È pensato per chi vuole orientarsi in
fretta: capire cosa mostrano i dati, dove sono solidi, quali limiti hanno e
 quali domande aiutano ad approfondire.

- **Stato:** alpha
- **Copertura:** 2023-2026, Italia
- **Unità di analisi:** Regione / Provincia / Impresa

## La domanda civica

**Quanto passa da Consip (convenzioni, accordi quadro, MePA, gare ASP) per settore e regione, e quali sono le imprese che partecipano attivamente?**

Esempi:
- Le regioni del Sud pagano di più per le utility in convenzione?
- Dove si concentrano le imprese con contratti attivi Consip?
- Le gare ASP sono concentrate nelle grandi città?

Le domande secondarie emergono in Discussions e diventano issue operative.

## Dataset

| Slug | Cosa contiene | Anni | Righe/anno | Stato |
|---|---|---|---|---|
| `consip-consumi-convenzione` | Spesa utility PA per convenzione | 2023-2025 | 8.000 | ✅ |
| `consip-bandie-gare` | Bandi e gare del Programma | 2024-2026 | 1.800 | ✅ |
| `consip-operatorieconomici` | Anagrafica imprese con attività Consip | 2024-2026 | 243.000 | ✅ |
| `consip-gareasp` | Gare ASP geolocalizzate | 2024-2026 | 16.000 | ✅ |

Definizioni dettagliate: [`docs/data_dictionary.md`](docs/data_dictionary.md)

## Support dataset

Le anagrafiche e i dizionari condivisi vivono in `support/` (es. lista comuni,
codici gestionali, classificazioni). Si eseguono prima dei dataset principali
con `make seeds`.

## Perché fidarsi

- fonti ufficiali o verificabili ([`docs/sources.md`](docs/sources.md))
- trasformazioni documentate ([`docs/decisions.md`](docs/decisions.md))
- controlli automatici prima della pubblicazione (CI + contract test)
- standard condivisi del DataCivicLab ([`.github`](https://github.com/dataciviclab/.github))

## Partecipa

- **Discussions** → domande civiche, interpretazioni, proposte di metriche
- **Issues** → bug, problemi tecnici, miglioramenti della pipeline

```
domanda civica → Discussion → Issue → analisi / notebook / output
```

Se non sei tecnico, parti da una **Discussion**: spiega contesto, territorio,
anno e cosa vuoi capire. Se la domanda richiede lavoro concreto, diventa una
**Issue** nella repo giusta (dataset qui, runtime nel toolkit, governance nelle
repo di ecosistema).

## Cos'è questa repo

È il repo operativo che nasce da `project-template` (il template standard del
Lab, modello multi-dataset, ADR-001):

- `datasets/` + `support/` — contratti dei dataset (`dataset.yml` + `sql/`)
- `Makefile` — interfaccia stabile: `make seeds`, `make run`, `make check`
- `requirements.txt` — dipendenze runtime (dataset puro)
- `docs/` — documentazione locale
- `tests/` — contract tests minimi
- `.github/` — workflow condivisi (check, pipeline, test-audit)

Un repo nato da questo template non serve solo a "ospitare dati": risponde in
modo verificabile a una domanda civica centrale.

## Confine con il toolkit

Il motore della pipeline vive nel repository `toolkit`. Questa repo non replica
la logica di esecuzione: definisce input, regole e output attesi per ogni dataset.

- bug o feature di CLI, runner, validazioni runtime → repo `toolkit`
- bug o modifiche a fonti, mapping, SQL, mart, docs → questa repo

## Da dove partire

Se stai clonando il template per un nuovo progetto:

1. aggiorna la domanda civica e gli esempi di insight
2. rinomina o sostituisci `datasets/demo-saldi-stato/` con i tuoi dataset
3. aggiungi le anagrafiche condivise in `support/`
4. aggiorna `<repo-slug>` nei workflow (bucket GCS e prefix registry)
5. aggiorna la riga `schedule` del pipeline alle cadenze del dataset
6. esegui `make check` e `python -m pytest tests/`

La struttura resta invariata. Non serve capire tutto subito.

## Esecuzione tecnica

```bash
pip install -r requirements.txt
make check        # valida tutti i dataset.yml (preflight)
make seeds        # esegue i support dataset
make run          # esegue tutti i dataset (RAW → CLEAN → MART)
python -m pytest tests/
```

Nota di contratto:

- i path relativi in `dataset.yml` sono risolti rispetto alla directory del
  file (ogni dataset ha `root: "../../out"`), non al cwd
- `metadata.json` è il payload ricco del layer; `manifest.json` il summary stabile
- `out/data/_runs/.../<run_id>.json` è il run record letto da `status`

Per dettagli più profondi su CLI e contratti: repo `toolkit`.

## Dove andare per il resto

- contesto del Lab, mappa delle repo, catalogo dataset: `dataciviclab`
- policy comuni, onboarding GitHub, template: `.github`
- motore tecnico della pipeline: `toolkit`

Riferimenti rapidi: [`docs/lab_links.md`](docs/lab_links.md)

## Ritmo operativo consigliato

1. una domanda civica principale sempre visibile nel README
2. domande complementari che si chiariscono in Discussions
3. issue piccole per trasformare le domande mature in lavoro concreto
4. output condivisibili pubblicati con continuità (pipeline + registry)

L'output non deve essere sempre una dashboard completa: può essere una risposta
breve con una tabella, un notebook che chiude una domanda precisa, un
aggiornamento su limiti e dati mancanti.
