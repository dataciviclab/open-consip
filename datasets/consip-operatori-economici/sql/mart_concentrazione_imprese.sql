select
  anno_riferimento,
  regione_sede_legale,
  forma_societaria,
  count(*) as n_imprese,
  sum(numero_aggiudicazioni) as n_aggiudicazioni_totale,
  sum(numero_contratti_attivi) as n_contratti_attivi_totale,
  sum(case when numero_aggiudicazioni > 0 then 1 else 0 end) as n_imprese_con_agg,
  sum(case when numero_aggiudicazioni > 0 then 1 else 0 end) * 100.0 / count(*) as pct_imprese_con_agg,
  avg(latitudine_sede_legale) as lat_media,
  avg(longitudine_sede_legale) as lon_media
from clean_input
group by
  anno_riferimento,
  regione_sede_legale,
  forma_societaria
order by
  anno_riferimento,
  n_aggiudicazioni_totale desc
