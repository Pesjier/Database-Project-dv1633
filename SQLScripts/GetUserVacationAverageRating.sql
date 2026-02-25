DROP PROCEDURE IF EXISTS get_user_vacation_average_rating;

CREATE PROCEDURE get_user_vacation_average_rating(uID INT)
	SELECT AVG(ratings.rating) as averageRating, ratings.vacationID, startDate, endDate
    FROM ratings
    JOIN (SELECT vacations.vacationID, vacations.startDate, vacations.endDate
    FROM vacations
    WHERE vacations.userID = uID) as userVacationsTable ON userVacationsTable.vacationID = ratings.vacationID
    GROUP BY userVacationsTable.vacationID;