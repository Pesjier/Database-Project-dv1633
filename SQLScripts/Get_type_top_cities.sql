CREATE PROCEDURE get_type_top_cities(act_type varchar(255))
	SELECT AVG(rating) as avgRating, cities.cityName, cities.cityID
    FROM cities
    JOIN (SELECT activities.activityType, activities.cityID, ratings.rating
    FROM activities
    JOIN ratings ON activities.activityID = ratings.activityID
    WHERE activities.activityType = act_type) as activitiesTable
    ON activitiesTable.cityID = cities.cityID
    GROUP BY cities.cityID
    ORDER BY avgRating DESC LIMIT 50