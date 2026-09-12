select
  anno_riferimento,
  tipo_strumento,
  criterio_aggiudicazione,
  count(*) as n_lotti,
  sum(base_asta) as base_asta_totale,
  avg(percentuale_erosione) as erosione_media,
  avg(numero_operatori_economici_partecipanti) as n_operatori_medio
from clean_input
group by
  anno_riferimento,
  tipo_strumento,
  criterio_aggiudicazione
order by
  anno_riferimento,
  tipo_strumento,
  criterio_aggiudicazione
