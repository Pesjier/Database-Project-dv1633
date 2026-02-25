DROP procedure IF EXISTS get_countries_avg_rate;
DELIMITER $$
CREATE procedure get_countries_avg_rate(IN act_id int) 
BEGIN
	SELECT AVG(rating), activities.activityType, countries.countryID, countries.countryName 
    FROM ratings
    JOIN activities on ratings.activityID = activities.activityID
    JOIN cities on activities.cityID = cities.cityID
    JOIN countries on cities.countryID = countries.countryID
    WHERE ratings.activityID = act_id
    GROUP BY ratings.activityID;
END; $$