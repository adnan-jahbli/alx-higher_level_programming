-- A script that uses the hbtn_0d_tvshows
-- database to list all genres not linked to the show Dexter
SELECT ge.name
FROM tv_genres AS ge
WHERE ge.name NOT IN (SELECT g.name
	FROM tv_genres g
	INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
	INNER JOIN tv_shows s ON s.id = sg.show_id
	WHERE s.title = 'Dexter')
ORDER BY ge.name ASC;
