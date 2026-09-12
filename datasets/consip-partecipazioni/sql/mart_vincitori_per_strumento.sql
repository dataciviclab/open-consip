select
  anno_riferimento,
  tipo_strumento,
  esito_partecipazione,
  count(*) as n_partecipazioni,
  count(distinct partita_iva) as n_imprese_distinte,
  count(distinct identificativo_lotto) as n_lotti_distinti
from clean_input
group by
  anno_riferimento,
  tipo_strumento,
  esito_partecipazione
order by
  anno_riferimento,
  n_partecipazioni desc
