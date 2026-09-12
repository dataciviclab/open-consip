select
  anno_riferimento,
  regione_pa,
  provincia_pa,
  stato_gara,
  count(*) as n_gare,
  sum(base_asta) as base_asta_totale,
  sum(valore_aggiudicato) as valore_aggiudicato_totale,
  avg(numero_fornitori_partecipanti) as n_fornitori_medio,
  sum(case when stato_gara = 'Gara aggiudicata definitivamente' then 1 else 0 end) * 100.0 / count(*) as tasso_aggiudicazione_pct,
  sum(case when stato_gara = 'Gara aggiudicata definitivamente' then valore_aggiudicato else 0 end) * 100.0 / nullif(sum(base_asta), 0) as incidenza_sul_prezzo_pct,
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
  n_gare desc
