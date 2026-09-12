select
  anno_riferimento,
  bando_mepa,
  sum(valore_ordini) as valore_ordini,
  count(*) as n_righe
from clean_input
where valore_ordini > 0
group by anno_riferimento, bando_mepa
order by valore_ordini desc
