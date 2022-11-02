-- script displays average temperature ordered by temp in
SELECT city, AVG(temperature) `avg_temp` FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
