DROP PROCEDURE IF EXISTS get_city_activity_type_ratings;

CREATE PROCEDURE get_city_activity_type_ratings(city INT)
	SELECT AVG(rating) as averageRating, activityType
    FROM (SELECT ratings.rating, activities.activityType, activities.cityID
	FROM ratings
    JOIN activities on ratings.activityID = activities.activityID) as tableName
	WHERE tableName.cityID = city
    GROUP BY activityType
	ORDER BY averageRating DESC;