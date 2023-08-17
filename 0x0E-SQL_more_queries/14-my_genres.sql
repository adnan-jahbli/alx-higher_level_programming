-- A script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter.
SELECT g.name
FROM tv_genres g
INNER JOIN tv_show_genres gs ON g.id = gs.genre_id
WHERE gs.show_id = (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = 'Dexter')
ORDER BY g.name ASC
