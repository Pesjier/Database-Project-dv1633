DROP PROCEDURE IF EXISTS get_country_activity_type_ratings;

CREATE PROCEDURE get_country_activity_type_ratings(country INT)
	SELECT AVG(ratings.rating) AS averageRating, activityType
    FROM ratings
    JOIN (SELECT activityID, activityType
    FROM Activities
    JOIN (SELECT cityID
    FROM cities
    WHERE country = cities.countryID) AS countryCities 
    ON countryCities.cityID = activities.cityID) as countryActivities
    ON countryActivities.activityID = ratings.activityID
    GROUP BY activityType;
