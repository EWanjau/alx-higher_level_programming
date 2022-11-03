-- join two tables and get a mysql query
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.id=states.id;
