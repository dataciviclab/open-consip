select
  anno_riferimento,
  regione_pa,
  provincia_pa,
  stato_gara,
  count(*) as n_gare,
  sum(base_asta) as base_asta_totale,
  sum(valore_aggiudicato) as valore_aggiudicato_totale,
  avg(numero_fornitori_partecipanti) as n_fornitori_medio,
  avg(latitudine_pa) as lat_media,
  avg(longitudine_pa) as lon_media
from clean_input
group by
  anno_riferimento,
  regione_pa,
  provincia_pa,
  stato_gara
order by
  anno_riferimento,
  regione_pa,
  provincia_pa,
  stato_gara
