# Consip — Ordini Diretti in Convenzione

## Domanda quida

**Quanto spende la PA italiana per convenzione Consip e per quali beni/servizi?**
La spesa per convenzione copre solo utility o anche altri beni? Quali convenzioni generano più ordini?

## Fonte

- **Ente**: Consip SpA / MEF
- **Dataset**: ORDINI DIRETTI DI ACQUISTO IN CONVENZIONE
- **Formato**: CSV, latin-1
- **Anni disponibili**: 2024, 2025, 2026
- **Licenza**: CC-BY-4.0

## Perimetro

- **Granularità**: convenzione × lotto × bene_servizio
- **Chiavi**: convenzione, lotto, codice_cpv
- **Cosa contiene**: ordini diretti effettuati dalla PA tramite convenzioni Consip (tutti i beni, non solo utility)

## Differenza con consumi-convenzione

- `consumi-convenzione`: solo utility (energia, gas, carburanti)
- `ordini-convenzione`: tutti i beni e servizi acquistati via convenzione

## Join

- `consumi-convenzione` su (regione_pa, convenzione, lotto) — per confrontare utility vs totale
- `bandi-e-gare` su (convenzione, lotto)
- `amministrazioni` su (regione_pa, provincia_pa)

## Stato

- **Pipeline**: in test
