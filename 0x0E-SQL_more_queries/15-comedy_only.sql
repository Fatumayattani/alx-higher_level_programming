-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- record should display: tv_shows.title.
-- sorted in ascending order by the show title.
SELECT t.`title`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;
