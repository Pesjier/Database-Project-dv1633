DROP PROCEDURE IF EXISTS get_city_name;

CREATE PROCEDURE get_city_name(city INTEGER)
	SELECT cityName
    FROM cities
    WHERE cities.cityID = city;