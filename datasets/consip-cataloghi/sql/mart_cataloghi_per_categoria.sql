select
  tipo_strumento,
  categoria_merceologica,
  count(*) as n_prodotti,
  count(distinct codice_cpv) as n_cpv_distinti,
  count(distinct identificativo_lotto) as n_lotti_distinti
from clean_input
group by tipo_strumento, categoria_merceologica
order by n_prodotti desc
