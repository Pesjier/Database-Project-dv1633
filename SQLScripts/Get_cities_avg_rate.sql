DROP procedure IF EXISTS get_cities_avg_rate;
DELIMITER $$
CREATE procedure get_cities_avg_rate(IN act_id int) 
BEGIN
	SELECT AVG(rating), activities.activityType, cities.cityID, cities.cityName 
    FROM ratings
    JOIN activities on ratings.activityID = activities.activityID
    JOIN cities on activities.cityID = cities.cityID
    WHERE ratings.activityID = act_id
    group by ratings.activityID;
END; $$
