DROP PROCEDURE IF EXISTS get_city_top_activities;

CREATE PROCEDURE get_city_top_activities(city INTEGER, minRatings INT, fromIndex INT, toIndex INT)
	SELECT averageRating, activityName, amountOfRatings
	FROM
		(SELECT * 
		FROM (SELECT AVG(ratings.rating) as averageRating, activities.activityName, activities.cityID, COUNT(ratings.rating) as amountOfRatings
			FROM ratings
			JOIN activities ON ratings.activityID = activities.activityID
			GROUP BY activities.activityID) as tablename
		WHERE amountOfRatings > minRatings) as anotherTableName
	WHERE city = anotherTableName.cityID
	ORDER BY averageRating DESC
	LIMIT fromIndex, toIndex;