-- lists all genres and number of shows linked to each
SELECT name , COUNT(tv_show_genres.show_id) `number_of_shows`
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
