DROP PROCEDURE IF EXISTS get_country_top_cities;

CREATE PROCEDURE get_country_top_cities(country INT, minRatings INT, fromIndex INT, toIndex INT)
	SELECT *
    FROM
    (SELECT AVG(ratings.rating) AS averageRating, cityName, COUNT(ratings.rating) as amountOfRatings
    FROM ratings
    JOIN (SELECT activityID, activityType, countryCities.cityID, cityName
    FROM Activities
    JOIN (SELECT cityID, cityName
    FROM cities
    WHERE country = cities.countryID) AS countryCities 
    ON countryCities.cityID = activities.cityID) as countryActivities
    ON countryActivities.activityID = ratings.activityID
    GROUP BY cityId) AS ratingTable
    WHERE amountOfRatings > minRatings
    ORDER BY averageRating DESC
	LIMIT fromIndex, toIndex;