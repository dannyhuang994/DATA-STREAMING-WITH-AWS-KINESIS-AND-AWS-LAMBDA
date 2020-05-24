SELECT Name, round(high,2) as High, ts as Time, hour as Hour
from(
  select stock_data.*,SUBSTRING(ts, 12, 2) as Hour, ROW_NUMBER() OVER(PARTITION BY name, SUBSTRING(ts, 12, 2) order by high) as rn
  FROM stock_data
)db1 where rn=1 order by name, Time
