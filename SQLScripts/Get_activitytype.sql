DROP procedure IF EXISTS get_activitytype;
DELIMITER $$
CREATE procedure get_activitytype(IN act_id int) 
BEGIN
	SELECT activityType
    FROM activities
    WHERE activityID = act_id;
END; $$