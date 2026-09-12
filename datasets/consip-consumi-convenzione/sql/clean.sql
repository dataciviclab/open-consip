select
  {year}::INTEGER as anno_riferimento,
  normalize_string("Tipologia_Amministrazione") as tipologia_amministrazione,
  normalize_string("Regione_PA") as regione_pa,
  normalize_string("Provincia_PA") as provincia_pa,
  normalize_string("Sigla_provincia_PA") as sigla_provincia_pa,
  normalize_string("Regione_Fornitore") as regione_fornitore,
  normalize_string("Convenzione") as convenzione,
  normalize_string("Lotto") as lotto,
  normalize_italian_number("Valore_economico_consumi") as valore_economico_consumi,
  cast_bigint("Numero_Ordini_con_consumi") as numero_ordini_con_consumi,
  cast_bigint("N_PA_con_consumi") as n_pa_con_consumi,
  cast_bigint("N_PO_con_consumi") as n_po_con_consumi
from raw_input
