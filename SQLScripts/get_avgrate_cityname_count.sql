DROP PROCEDURE get_city_avg_ratae_count_users;
delimiter $$
create procedure get_city_avg_ratae_count_users(IN aID INT)
begin
Select cityname, avg(ratings.rating) as averagerating, count(ratings.activityID) as numberofratings
	from cities
	join activities on activities.cityID = cities.cityID
	join ratings on ratings.activityID = activities.activityID
	where ratings.activityID = aID
	group by cities.cityID, cities.cityName
	order by averagerating desc;
end $$
delimiter ;

