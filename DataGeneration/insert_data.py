import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=""
)

######################################################################
#countries
def countries_insert():
  mycursor = mydb.cursor()
  country_data = set() #countries data
  sql = "INSERT INTO countries (countryId, countryName) VALUES (%s, %s)"
  with open("Countries.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      country_data.add((item[0], item[1]))

  mycursor.executemany(sql, list(country_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("country data done")

#####################################################################

#cities
def cities_insert():
  mycursor = mydb.cursor()
  city_data = set() #cities data
  sql = "INSERT INTO cities (cityID, cityName, countryId) VALUES (%s, %s, %s)"
  with open("Cities.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      city_data.add((item[0], item[1], item[2]))
  
  mycursor.executemany(sql, list(city_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("city data done")

################################################################
#Users
def user_insert():
  mycursor = mydb.cursor()
  user_data = set() #users data
  sql = "INSERT INTO users (userId, userName, countryId) VALUES (%s, %s, %s)"
  with open("Users.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      user_data.add((item[0], item[1], item[2]))
  
  mycursor.executemany(sql, list(user_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("user data done")

#########################################################
#Activities

def activities_insert():
  mycursor = mydb.cursor()
  activity_data = set() #activities data
  sql = "INSERT INTO activities (activityId, activityName, activityType, cityId) VALUES (%s, %s, %s, %s)"
  with open("Activities.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      activity_data.add((item[0], item[1], item[2], item[3]))
  
  mycursor.executemany(sql, list(activity_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("Activities am done")

#########################################################
#Vacations

def vacation_insert():
  mycursor = mydb.cursor()
  vacation_data = set() #vacation data
  sql = "INSERT INTO vacations (vacationId, startDate, endDate, userId) VALUES (%s, %s, %s, %s)"
  with open("Vacations.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      item[1] = item[1].strip('"')
      item[2] = item[2].strip('"')
      vacation_data.add((item[0], item[1], item[2], item[3]))
  
  mycursor.executemany(sql, list(vacation_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("vacation done")

#################################################################
#Ratings
rating_data = set() #rating data
def create_data_rating ():
  checking_data =set() #it is checking if the primary key already exist
  with open("Ratings.csv", encoding="utf-8") as f:
    for i in f:
      i = i.strip().split(",")
      check_data = (i[0], i[1])
      if check_data not in checking_data:
        checking_data.add(check_data)
        rating_data.add((i[0], i[1], i[2]))
  
  rating_insert()
  


def rating_insert():

  mycursor = mydb.cursor()

  sql = "INSERT INTO ratings (activityId, vacationId, rating) VALUES (%s, %s, %s)"       
  mycursor.executemany(sql, list(rating_data))
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("ratings done")


if __name__ == "__main__":
  countries_insert()
  cities_insert()
  user_insert()
  activities_insert()
  vacation_insert()
  create_data_rating()