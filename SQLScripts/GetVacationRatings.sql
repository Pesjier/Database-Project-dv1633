DROP PROCEDURE IF EXISTS get_vacation_ratings;

CREATE PROCEDURE get_vacation_ratings(vacation INT)
	SELECT rating, activities.activityID, activityName
    FROM activities
    JOIN (SELECT rating, activityID
    FROM ratings
    WHERE ratings.vacationID = vacation) as vacationRatings
    ON vacationRatings.activityID = activities.activityID
    ORDER BY rating DESC;