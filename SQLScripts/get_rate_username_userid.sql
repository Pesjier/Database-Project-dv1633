CREATE PROCEDURE get_username_rate_id(IN act_id int)
SELECT rating, users.userName, users.userID
FROM (SELECT rating, vacations.userID
FROM (SELECT ratings.vacationID, ratings.rating
FROM ratings
WHERE ratings.activityID = act_id) as activityRatings
JOIN vacations on vacations.vacationID = activityRatings.vacationID) as vacationRatings
JOIN users ON users.userID = vacationRatings.userID

