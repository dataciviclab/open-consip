select
  {year}::INTEGER as anno_riferimento,
  normalize_string("Tipologia_Amministrazione") as tipologia_amministrazione,
  normalize_string("Regione_PA") as regione_pa,
  normalize_string("Provincia_PA") as provincia_pa,
  normalize_string("Sigla_provincia_PA") as sigla_provincia_pa,
  normalize_string("Regione_Fornitore") as regione_fornitore,
  normalize_string("Bando_Mepa") as bando_mepa,
  normalize_string("Categoria_Abilitazione") as categoria_abilitazione,
  normalize_string("bene_servizio") as bene_servizio,
  normalize_string("codice_CPV") as codice_cpv,
  normalize_string("descrizione_CPV") as descrizione_cpv,
  cast_bigint("N_Ordini") as n_ordini,
  normalize_italian_integer("Valore_economico_Ordini") as valore_ordini,
  cast_bigint("N_PA") as n_pa,
  cast_bigint("N_fornitori") as n_fornitori,
  cast_bigint("N_PO") as n_po
from raw_input
