select
  anno_riferimento,
  regione_pa,
  tipo_negoziazione,
  sum(n_contratti_stipulati) as n_contratti,
  sum(valore_contratti_stipulati) as valore_contratti,
  avg(n_medio_fornitori_partecipanti) as fornitori_medi,
  avg(tempi_medi_stipula) as tempi_stipula_medio,
  avg(durata_media_negoziazione) as durata_negoziazione_media,
  sum(n_pa_appaltanti) as n_pa_totali
from clean_input
group by
  anno_riferimento,
  regione_pa,
  tipo_negoziazione
order by
  anno_riferimento,
  valore_contratti desc
