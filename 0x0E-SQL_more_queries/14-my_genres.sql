-- A script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter.
SELECT g.name
FROM tv_genres g
INNER JOIN tv_show_genres gs ON g.id = gs.genre_id
INNER JOIN tv_shows s ON s.id = gs.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
