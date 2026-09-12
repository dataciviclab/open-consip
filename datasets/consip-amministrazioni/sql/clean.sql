select
  {year}::INTEGER as anno_riferimento,
  cast_bigint("#Identificativo_Amministrazione") as identificativo_amministrazione,
  normalize_string("Identificativo_IPA_amministrazione") as identificativo_ipa,
  normalize_string("Tipologia_Amministrazione") as tipologia_amministrazione,
  normalize_string("Codice_Fiscale") as codice_fiscale,
  normalize_string("Denominazione") as denominazione,
  normalize_string("Regione") as regione,
  normalize_string("Provincia") as provincia,
  normalize_string("Comune") as comune,
  try_cast("Latitudine" as DOUBLE) as latitudine,
  try_cast("Longitudine" as DOUBLE) as longitudine,
  cast_bigint("Numero_PO_attivi") as numero_po_attivi
from raw_input
