select
  normalize_string("#Denominazione_Iniziativa") as denominazione_iniziativa,
  normalize_string("Denominazione_Lotto") as denominazione_lotto,
  normalize_string("Identificativo_Lotto") as identificativo_lotto,
  normalize_string("Tipo_Strumento") as tipo_strumento,
  normalize_string("Prodotto") as prodotto,
  normalize_string("Codice_CPV") as codice_cpv,
  normalize_string("Descrizione_CPV") as descrizione_cpv,
  normalize_string("Tipo_Prodotto") as tipo_prodotto,
  normalize_string("Categoria_Merceologica") as categoria_merceologica,
  normalize_string("Descrizione_Dettaglio") as descrizione_dettaglio,
  normalize_string("Principale_Accessorio") as principale_accessorio,
  normalize_string("Articolo_Disponibile_Mese_Corrente") as articolo_disp_mese,
  normalize_string("Articolo_Disponibile_Anno_Solare") as articolo_disp_anno
from raw_input
