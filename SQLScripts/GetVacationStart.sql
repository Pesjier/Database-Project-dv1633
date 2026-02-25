DROP FUNCTION IF EXISTS get_vacation_start

DELIMITER %%
CREATE FUNCTION get_vacation_start(vacation INT) RETURNS DATE DETERMINISTIC
BEGIN
	DECLARE sDate DATE;
    SET sDate = (SELECT startDate
    FROM vacations
    WHERE vacations.vacationID = vacation);
    RETURN sDate;
END %%