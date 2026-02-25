DROP FUNCTION IF EXISTS get_vacation_user

DELIMITER %%
CREATE FUNCTION get_vacation_user(vacation INT) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE uID INT;
    SET uID = (SELECT userID
    FROM vacations
    WHERE vacations.vacationID = vacation);
    RETURN uID;
END %%