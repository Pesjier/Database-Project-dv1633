import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="laura123",
  database="mysqlproject"
)

######################################################################
#countries
def countries_insert():
  mycursor = mydb.cursor()
  country_data = set() #countries data
  sql = "INSERT INTO countries (countryid, namn) VALUES (%s, %s)"
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Countries.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      country_data.add((item[0], item[1]))
  
  mycursor.executemany(sql, country_data)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("country data done")

#####################################################################

#cities
def cities_insert():
  mycursor = mydb.cursor()
  city_data = set() #cities data
  sql = "INSERT INTO cities (cityid, cityname, countryid) VALUES (%s, %s, %s)"
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Cities.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      city_data.add((item[0], item[1], item[2]))
  
  mycursor.executemany(sql, city_data)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("city data done")

################################################################
#Users
def user_insert():
  mycursor = mydb.cursor()
  user_data = set() #users data
  sql = "INSERT INTO users (userid, fullname, countryid) VALUES (%s, %s, %s)"
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Users.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      user_data.add((item[0], item[1], item[2]))
  
  mycursor.executemany(sql, user_data)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("user data done")

#########################################################
#Activities

def activities_insert():
  mycursor = mydb.cursor()
  activity_data = set() #activities data
  sql = "INSERT INTO activities (activityid, namn, activitytype, cityid) VALUES (%s, %s, %s, %s)"
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Activities.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      activity_data.add((item[0], item[1], item[2], item[3]))
  
  mycursor.executemany(sql, activity_data)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("Activities am done")

#########################################################
#Vacations

def vacation_insert():
  mycursor = mydb.cursor()
  vacation_data = set() #vacation data
  sql = "INSERT INTO vacation (vacationid, startdate, enddate, userid) VALUES (%s, %s, %s, %s)"
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Vacations.csv", encoding="utf-8") as f:
    for item in f:
      item = item.strip().split(",")
      item[1] = item[1].strip('"')
      item[2] = item[2].strip('"')
      vacation_data.add((item[0], item[1], item[2], item[3]))
  
  mycursor.executemany(sql, vacation_data)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  print("vacation done")

#################################################################
#Ratings
rating_data = set() #rating data
def create_data_rating ():
  checking_data =set() #it is checking if the primary key already exist
  with open("C:/Users/dshml/OneDrive/Documents/Database-Project-dv1633-main/Database-Project-dv1633/DataGeneration/Ratings.csv", encoding="utf-8") as f:
    for i in f:
      i = i.strip().split(",")
      check_data = (i[0], i[1])
      if check_data not in checking_data:
        checking_data.add(check_data)
        rating_data.add((i[0], i[1], i[2]))
  
  rating_insert()
  


def rating_insert():

  mycursor = mydb.cursor()

  sql = "INSERT INTO ratings (activityid, vacationid, rating) VALUES (%s, %s, %s)"       
  mycursor.executemany(sql, rating_data)
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