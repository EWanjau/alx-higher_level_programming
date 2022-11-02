-- lists top 3 cities in two months order by temperature descending
SELECT city, AVG(temp) avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city  ORDER BY avg_temp DESC LIMIT 3;
