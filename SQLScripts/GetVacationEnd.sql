DROP FUNCTION IF EXISTS get_vacation_end

DELIMITER %%
CREATE FUNCTION get_vacation_end(vacation INT) RETURNS DATE DETERMINISTIC
BEGIN
	DECLARE eDate DATE;
    SET eDate = (SELECT endDate
    FROM vacations
    WHERE vacations.vacationID = vacation);
    RETURN eDate;
END %%