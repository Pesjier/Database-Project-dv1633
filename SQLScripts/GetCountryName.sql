DROP FUNCTION IF EXISTS get_country_name;

DELIMITER %%
CREATE FUNCTION get_country_name(country INTEGER) RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	DECLARE cName VARCHAR(255);
    SET cName = 
	(SELECT countryName
    FROM countries
    WHERE countries.countryID = country);
    RETURN cName;
END; %%