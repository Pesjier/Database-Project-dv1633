DROP PROCEDURE get_country_avg_ratae_count_users;
delimiter $$
create procedure get_country_avg_ratae_count_users(IN aID INT)
begin
Select countryName, avg(ratings.rating) as averagerating, count(ratings.vacationID) as numberofratings
	from countries
	join cities on cities.countryID = countries.countryID
	join activities on activities.cityID = cities.cityID
	join ratings on ratings.activityID = activities.activityID
	where ratings.activityID = aID
	group by countries.countryID, countries.countryName
	order by averagerating desc;
end $$

delimiter ;

