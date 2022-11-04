-- list all values even the null values
SELECT title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;