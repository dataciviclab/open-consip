select
  anno_riferimento,
  regione,
  tipologia_amministrazione,
  count(*) as n_pa,
  sum(numero_po_attivi) as n_po_totali,
  avg(latitudine) as lat_media,
  avg(longitudine) as lon_media
from clean_input
group by
  anno_riferimento,
  regione,
  tipologia_amministrazione
order by
  anno_riferimento,
  n_pa desc
