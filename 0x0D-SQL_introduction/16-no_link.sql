-- a script that lists all records apart from the missing fields
SELECT score, name  FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
