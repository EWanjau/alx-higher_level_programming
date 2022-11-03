-- join two tables and get a mysql query
SELECT c.id, c.name, s.name FROM cities INNER JOIN states ON cities.id=states.id;
