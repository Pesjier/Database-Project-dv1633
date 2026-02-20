DROP TABLE Countries;
DROP TABLE Cities;
DROP TABLE Activities;
DROP TABLE Users;
DROP TABLE Vacations;
DROP TABLE Ratings;

CREATE TABLE Countries
(
	countryID int NOT NULL,
    countryName varchar(255),
    PRIMARY KEY(countryID)
);

CREATE TABLE Cities
(
	cityID int NOT NULL,
    cityName varchar(255),
    countryID int NOT NULL,
    PRIMARY KEY(cityID),
    FOREIGN KEY(countryID) REFERENCES Countries(countryID)
);

CREATE TABLE Users
(
	userID int NOT NULL,
    userName varchar(255),
    countryID int NOT NULL,
    PRIMARY KEY(userID),
    FOREIGN KEY(countryID) REFERENCES Countries(countryID)
);

CREATE TABLE Activities
(
	activityID int NOT NULL,
    activityName varchar(255),
    activityType varchar(255),
    cityID int NOT NULL,
    PRIMARY KEY(activityID),
    FOREIGN KEY(cityID) REFERENCES Cities(cityID)
);

CREATE TABLE Vacations
(
	vacationID int NOT NULL,
    startDate DATE,
    endDate DATE,
    userID int NOT NULL,
    PRIMARY KEY(vacationID),
    FOREIGN KEY(userID) REFERENCES Users(userID)
);

CREATE TABLE Ratings
(
	activityID int NOT NULL,
    vacationID int NOT NULL,
    rating int,
    CONSTRAINT ratingID PRIMARY KEY(activityID, vacationID)
);
