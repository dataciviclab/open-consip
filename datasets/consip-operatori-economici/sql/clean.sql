select
  {year}::INTEGER as anno_riferimento,
  normalize_string("#Partita_Iva") as partita_iva,
  normalize_string("Ragione_Sociale") as ragione_sociale,
  normalize_string("Forma_Societaria") as forma_societaria,
  normalize_string("Nazione_Sede_legale") as nazione_sede_legale,
  normalize_string("Regione_Sede_legale") as regione_sede_legale,
  normalize_string("Provincia_Sede_legale") as provincia_sede_legale,
  normalize_string("Comune_Sede_legale") as comune_sede_legale,
  normalize_string("Indirizzo_Sede_legale") as indirizzo_sede_legale,
  try_cast("Latitudine_Sede_legale" as DOUBLE) as latitudine_sede_legale,
  try_cast("Longitudine_Sede_legale" as DOUBLE) as longitudine_sede_legale,
  cast_bigint("Numero_Aggiudicazioni") as numero_aggiudicazioni,
  cast_bigint("Numero_Abilitazioni") as numero_abilitazioni,
  cast_bigint("Numero_Transazioni") as numero_transazioni,
  cast_bigint("Numero_Contratti_attivi") as numero_contratti_attivi
from raw_input
