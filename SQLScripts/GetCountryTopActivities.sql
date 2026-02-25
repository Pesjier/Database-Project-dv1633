DROP PROCEDURE IF EXISTS get_country_top_activities;

CREATE PROCEDURE get_country_top_activities(country INTEGER)
	SELECT averageRating, activityName, amountOfRatings
	FROM
		(SELECT * 
		FROM (SELECT AVG(ratings.rating) as averageRating, activities.activityName, activities.cityID, COUNT(ratings.rating) as amountOfRatings
			FROM ratings
			JOIN activities ON ratings.activityID = activities.activityID
			GROUP BY activities.activityID) as tablename
		WHERE amountOfRatings > 5) as anotherTableName
	JOIN (SELECT cityID
		FROM cities
		JOIN countries ON countries.countryID = cities.countryID
		where countries.countryID = country) AS countryCities ON countryCities.cityID = anotherTableName.cityID
	ORDER BY averageRating DESC;