DROP FUNCTION IF EXISTS get_country_of_city;

DELIMITER %%
CREATE FUNCTION get_country_of_city(city INTEGER) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE country INT;
	SET country=
    (SELECT countryID
    FROM cities
    WHERE cities.cityID = city);
    RETURN country;
END; %%