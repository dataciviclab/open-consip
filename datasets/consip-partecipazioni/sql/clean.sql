select
  {year}::INTEGER as anno_riferimento,
  normalize_string("#Denominazione_Iniziativa") as denominazione_iniziativa,
  normalize_string("Denominazione_Lotto") as denominazione_lotto,
  normalize_string("Identificativo_Lotto") as identificativo_lotto,
  normalize_string("Tipo_Strumento") as tipo_strumento,
  normalize_string("Partita_Iva") as partita_iva,
  normalize_string("Ragione_Sociale") as ragione_sociale,
  normalize_string("Forma_Partecipazione") as forma_partecipazione,
  normalize_string("Denominazione_Partecipazione") as denominazione_partecipazione,
  cast_bigint("Progressivo_Partecipante") as progressivo_partecipante,
  normalize_string("Flag_Capogruppo") as flag_capogruppo,
  normalize_string("Esito_Partecipazione") as esito_partecipazione,
  try_cast("Data_Aggiudicazione/Abilitazione" as DATE) as data_aggiudicazione
from raw_input
