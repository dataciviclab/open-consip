select
  anno_riferimento,
  regione_pa,
  provincia_pa,
  sigla_provincia_pa,
  tipologia_amministrazione,
  regione_fornitore,
  sum(valore_economico_consumi) as spesa_totale,
  sum(numero_ordini_con_consumi) as ordini_totali,
  count(distinct convenzione) as convenzioni_distinte,
  count(distinct lotto) as lotti_distinti,
  sum(n_pa_con_consumi) as pa_coinvolte,
  sum(n_po_con_consumi) as punti_prelievo
from clean_input
group by
  anno_riferimento,
  regione_pa,
  provincia_pa,
  sigla_provincia_pa,
  tipologia_amministrazione,
  regione_fornitore
order by
  anno_riferimento,
  regione_pa,
  provincia_pa,
  tipologia_amministrazione
