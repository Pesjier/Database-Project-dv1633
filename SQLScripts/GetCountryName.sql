DROP PROCEDURE IF EXISTS get_country_name;

CREATE PROCEDURE get_country_name(country INTEGER)
	SELECT countryName
    FROM countries
    WHERE countries.countryID = country;