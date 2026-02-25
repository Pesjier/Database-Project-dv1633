DROP procedure IF EXISTS getactivityname;
DELIMITER $$
CREATE procedure getactivityname(IN id int) 
BEGIN
	SELECT activityName, countries.countryname, cities.cityName
    FROM activities
    JOIN cities on activities.cityID = cities.cityID
    JOIN countries on cities.countryID = countries.countryID
    WHERE activities.activityID = id;
END; $$
