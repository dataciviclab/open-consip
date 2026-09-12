select
  anno_riferimento,
  convenzione,
  sum(importo_ordinato) as importo_totale,
  count(*) as n_righe,
  count(distinct lotto) as n_lotti_distinti,
  count(distinct codice_cpv) as n_cpv_distinti
from clean_input
where importo_ordinato > 0
group by
  anno_riferimento,
  convenzione
order by
  anno_riferimento,
  importo_totale desc
