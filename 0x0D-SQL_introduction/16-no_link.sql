-- script lists all records without the empty records
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
