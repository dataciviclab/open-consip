# Consip — Amministrazioni del Programma

## Domanda quida

**Quante PA sono attive su Consip e dove sono concentrate?**
L'anagrafica delle PA registrate su acquistinretepa.it con almeno un punto ordinante attivo rivela Concentrazioni territoriali o tipologiche?

## Fonte

- **Ente**: Consip SpA / MEF
- **Portale**: [dati.consip.it](https://dati.consip.it)
- **Dataset**: AMMINISTRAZIONI DEL PROGRAMMA
- **Formato**: CSV, delimitato `,`, encoding utf-8
- **Anni disponibili**: 2024, 2025, 2026
- **Licenza**: CC-BY-4.0

## Perimetro

- **Granularità**: amministrazione (una riga = una PA con almeno 1 PO attivo)
- **Chiavi**: identificativo_amministrazione, IPA, codice_fiscale
- **Cosa contiene**: anagrafica PA con codice IPA, tipologia, geo, numero punti ordinanti attivi

## Utilità

Support dataset universale — join con tutti gli altri dataset CONSIP via IPA o geo.

## Stato

- **Pipeline**: in test
