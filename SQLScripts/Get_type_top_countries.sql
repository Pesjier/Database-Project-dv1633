DROP PROCEDURE IF EXISTS get_type_top_countries;

CREATE PROCEDURE get_type_top_countries(act_type varchar(255))
	SELECT countries.countryName, countries.countryID, AVG(rating) as avgRating
    FROM countries
    JOIN (SELECT cities.countryID, rating
    FROM cities
    JOIN (SELECT activities.activityType, activities.cityID, ratings.rating
    FROM activities
    JOIN ratings ON activities.activityID = ratings.activityID
    WHERE activities.activityType = act_type) as activitiesTable
    ON activitiesTable.cityID = cities.cityID) as citiesTable
    WHERE citiesTable.countryID = countries.countryID
    GROUP BY countries.countryID
    ORDER BY avgRating DESC LIMIT 50;