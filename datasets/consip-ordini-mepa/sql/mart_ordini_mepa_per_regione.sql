select
  anno_riferimento,
  regione_pa,
  sum(valore_ordini) as valore_ordini,
  count(*) as n_righe
from clean_input
where valore_ordini > 0
group by anno_riferimento, regione_pa
order by valore_ordini desc
