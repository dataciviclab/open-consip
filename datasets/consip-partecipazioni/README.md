# Consip — Partecipazioni

## Domanda quida

**Chi vince le gare Consip e con che esito?**
Le imprese che partecipano alle iniziative Consip sono concentrate in poche grandi o distribuite? L'esito delle partecipazioni rivela pattern di competizione?

## Fonte

- **Ente**: Consip SpA / MEF
- **Dataset**: PARTECIPAZIONI
- **Formato**: CSV, utf-8
- **Anni disponibili**: 2024, 2025, 2026
- **Licenza**: CC-BY-4.0

## Perimetro

- **Granularità**: partecipazione (una riga = un'impresa che partecipa a un lotto)
- **Chiavi**: identificativo_lotto, partita_iva, esito
- **Cosa contiene**: imprese partecipanti a iniziative (Convenzioni, AQ, MePA, ASP), con esito (aggiudicatario, abilitato, ecc.)

## Join

- `bandi-e-gare` ↔ `partecipazioni` su (identificativo_lotto)
- `partecipazioni` ↔ `operatori-economici` su (partita_iva)
- `partecipazioni` ↔ `amministrazioni` su (geo o IPA, indiretto)

## Stato

- **Pipeline**: in test
