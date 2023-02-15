-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- record should display: tv_shows.title - rating sum.
-- sorted in descending order by the rating.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
