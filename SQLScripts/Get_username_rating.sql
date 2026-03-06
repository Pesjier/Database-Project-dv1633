
CREATE PROCEDURE get_username_rate(IN vID INT)

	SELECT users.userName, rating, users.userID
    FROM ratings
    JOIN vacations on ratings.vacationID = vacations.vacationID
    JOIN users on vacations.userID = users.userID
    WHERE ratings.vacationID = vID;

