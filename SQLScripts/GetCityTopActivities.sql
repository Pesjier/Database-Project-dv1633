DROP PROCEDURE IF EXISTS get_city_top_activities;

CREATE PROCEDURE get_city_top_activities(city INTEGER)
	SELECT averageRating, activityName, amountOfRatings
	FROM
		(SELECT * 
		FROM (SELECT AVG(ratings.rating) as averageRating, activities.activityName, activities.cityID, COUNT(ratings.rating) as amountOfRatings
			FROM ratings
			JOIN activities ON ratings.activityID = activities.activityID
			GROUP BY activities.activityID) as tablename
		WHERE amountOfRatings > 0) as anotherTableName
	WHERE city = anotherTableName.cityID
	ORDER BY averageRating DESC;