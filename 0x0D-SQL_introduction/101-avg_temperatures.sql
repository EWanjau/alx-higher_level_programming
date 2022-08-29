-- displays temp and area grouped
SELECT city, avg(value) avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC

