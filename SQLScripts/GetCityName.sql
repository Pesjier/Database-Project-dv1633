DROP FUNCTION IF EXISTS get_city_name;

DELIMITER %%
CREATE FUNCTION get_city_name(city INTEGER) RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	DECLARE cName VARCHAR(255);
    SET cName = 
	(SELECT cityName
    FROM cities
    WHERE cities.cityID = city);
    RETURN cName;
END; %%