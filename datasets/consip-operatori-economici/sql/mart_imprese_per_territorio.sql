select
  anno_riferimento,
  regione_sede_legale,
  forma_societaria,
  count(*) as n_imprese,
  sum(numero_aggiudicazioni) as numero_aggiudicazioni_totale,
  sum(numero_contratti_attivi) as numero_contratti_attivi_totale,
  avg(latitudine_sede_legale) as lat_media,
  avg(longitudine_sede_legale) as lon_media
from clean_input
group by
  anno_riferimento,
  regione_sede_legale,
  forma_societaria
order by
  anno_riferimento,
  regione_sede_legale,
  forma_societaria
