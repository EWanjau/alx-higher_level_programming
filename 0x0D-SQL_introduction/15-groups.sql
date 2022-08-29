-- lists all records with the same score
SELECT score, COUNT(score) `number` FROM second_table GROUP BY score ORDER BY number DESC
