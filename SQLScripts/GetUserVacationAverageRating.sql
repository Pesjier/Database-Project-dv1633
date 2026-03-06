CREATE PROCEDURE get_user_vacation_average_rating(uID INT)
	SELECT *
	FROM (SELECT AVG(ratings.rating) as averageRating, ratings.vacationID, startDate, endDate, users.userName, users.userID
    FROM ratings
    JOIN vacations on ratings.vacationID = vacations.vacationID
    JOIN users on vacations.userID = users.userID
    GROUP BY vacationID) as tableName
    WHERE tableName.userID = uID;
