DROP procedure IF EXISTS getavg_rate_count;
DELIMITER $$
CREATE procedure getavg_rate_count(IN act_id int) 
BEGIN
	SELECT AVG(rating) as avgRating, COUNT(rating) as count_rate
    FROM ratings
    where activityID = act_id
    group by activityID; 
END; $$
