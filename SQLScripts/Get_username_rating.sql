DROP procedure IF EXISTS get_username_rate;
DELIMITER $$
CREATE procedure get_username_rate(IN vac_id int) 
BEGIN
	SELECT users.userName, rating
    FROM ratings
    JOIN vacations on ratings.vacationID = vacations.vacationID
    JOIN users on vacations.userID = users.userID
    WHERE ratings.vacationID = vac_id;
END; $$

