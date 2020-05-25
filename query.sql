-- note that stock_data should be the name of your table from database 
SELECT upper(db1.Name) AS Name, round(db1.High,2) AS High, db1.Hour as Hour, ts AS Timestamp 
FROM (
  SELECT name AS Name, max(high) AS High, substring(ts,12,2) AS Hour
  FROM  stock_data GROUP BY 1, 3 ORDER BY 1, 3
  )db1, stock_data db2
WHERE db1.Name = db2.name AND db1.Hour = substring(ts,12,2) AND db1.high = db2.High
ORDER BY Name, Hour;

