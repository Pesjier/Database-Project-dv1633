DROP PROCEDURE IF EXISTS get_user_vacation_average_rating;

CREATE PROCEDURE get_user_vacation_average_rating(uID INT)
	SELECT AVG(ratings.rating) as averageRating, ratings.vacationID, startDate, endDate, users.userName
    FROM ratings
    JOIN (SELECT vacations.vacationID, vacations.startDate, vacations.endDate
    FROM vacations
    WHERE vacations.userID = uID) as userVacationsTable ON userVacationsTable.vacationID = ratings.vacationID
    JOIN users on vacations.userID = userID.userID
    GROUP BY userVacationsTable.vacationID;
    
call get_user_vacation_average_rating(2);