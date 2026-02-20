import random
import datetime

#Country
countrylist =[] 

#City
citylist = []
cityCountry = []

#Activity
activitylist = []
activityCity = []
activityType = []
#laura
#Users
userlist = []
userCountry = []

#Vacations
vacationStart = []
vacationEnd = []
vacationUser = []

#Vacation Activities
takenActivityVacation = []
takenActivity = []
takenActivityRating = []

#Helper
acvitivitesInCountry = []

#Hämta länder och spara lokalt i variabel
#Hämta städer och spara lokalt i variabel, ska peka på land
def CreateCountry(name):
  countrylist.append(name)
  acvitivitesInCountry.append([])

def CreateCity(name, country):
  if(not country in countrylist): #If country doesnt exist, create it    
    CreateCountry(country)
  citylist.append(name) #Add city to list
  countryIndex = countrylist.index(country)
  cityCountry.append(countryIndex) #Add index of country to cityCountry list

with open("worldcities.csv", encoding="utf-8") as f:
  for line in f:
    line = line.replace('"', '')
    values = line.split(',')
    CreateCity(values[0], values[4])

#Skapa aktiviteter och spara lokalt i variabel, ska peka på stad
activityTypes = ["Restaurant", "Bar", "Museum", "Hotel", "Tourist Attraction"]

cityIndex = 0
for city in citylist:
  countryyyy = cityCountry[cityIndex]
  for activity in activityTypes:
    activitylist.append(city + " " + activity)
    activityType.append(activity)
    activityCity.append(cityIndex)
    acvitivitesInCountry[countryyyy].append(len(activitylist) - 1)
  cityIndex += 1

#Skapa användare, ska ha ett land, namn
firstNames = []
lastNames = []

def OnlyLetters(char):
  if ord(char) < 65 or ord(char) > 122:
    return ''
  return char

#Hämta first names
with open("FirstNames.txt") as f:
  for line in f:
    filtered = ''.join(filter(OnlyLetters, line))
    firstNames.append(filtered)

#Hämta last names
with open("LastNames.txt", encoding="utf-8") as f:
  for line in f:
    values = line.split('	') #Special type of space : )
    filtered = ''.join(filter(OnlyLetters, values[len(values) - 1]))
    lastNames.append(filtered)

#Skapa users
userIndex = 0
while userIndex < 10000:
  name = firstNames[random.randint(0, len(firstNames) - 1)] + " " + lastNames[random.randint(0, len(lastNames) - 1)]
  userlist.append(name)
  userCountry.append(random.randint(0, len(countrylist) - 1))
  userIndex += 1

#Skapa Vacations, ska ha random aktiviteter från ett random land
vacationIndex = 0
while vacationIndex < 50000:
  #Decide duration and dates
  randomYear = random.randint(2000, 2025)
  randomMonth = random.randint(1, 12)
  randomDay = random.randint(1, 24)

  randomDuration = random.randint(1, 90)

  startDate = datetime.datetime(randomYear, randomMonth, randomDay)
  endDate = startDate + datetime.timedelta(days=randomDuration)
  
  startDateString = '"' + str(startDate.date()) + '"'
  endDateString = '"' + str(endDate.date()) + '"'
  vacationStart.append(startDateString)
  vacationEnd.append(endDateString)

  #Choose user
  vacationUser.append(random.randint(0, len(userlist) - 1))

  #Choose Activities and rate them
  chosenCountry = random.randint(0, len(countrylist) - 1)
  #print(countrylist[chosenCountry])

  activityAmount = random.randint(1, 5)
  activityIndex = 0
  while activityIndex < activityAmount:
    # chosenActivity = countryActivities[random.randint(0, len(countryActivities) - 1)]
    chosenActivity = acvitivitesInCountry[chosenCountry][random.randint(0, len(acvitivitesInCountry[chosenCountry]) - 1)]
    takenActivityVacation.append(vacationIndex)
    takenActivity.append(chosenActivity)
    takenActivityRating.append(random.randint(1, 5))
    activityIndex += 1

    #print(activitylist[chosenActivity])

  vacationIndex += 1
print("Done creating data")

print("Creating files!")
#Spara allt i filer
#Countries.csv
with open("Countries.csv", "w", encoding="utf-8") as f:
  index = 0
  for country in countrylist:
    f.write(str(index)) #Primary key index
    f.write(",")
    f.write(country) #Name attribute
    f.write('\n') #New line
    index += 1

#Cities.csv
with open("Cities.csv", "w", encoding="utf-8") as f:
  index = 0
  for city in citylist:
    f.write(str(index)) #Primary key index
    f.write(",")
    f.write(city) #Name attribute
    f.write(",")
    f.write(str(cityCountry[index])) #Foreign key to country
    f.write('\n') #New line
    index += 1

#Activities.csv
with open("Activities.csv", "w", encoding="utf-8") as f:
  index = 0
  for activity in activitylist:
    f.write(str(index)) #Primary key index
    f.write(",")
    f.write(activity) #Name attribute
    f.write(",")
    f.write(activityType[index]) #Type attribute
    f.write(",")
    f.write(str(activityCity[index])) #Foreign key to city
    f.write('\n') #New line
    index += 1

#Users.csv
with open("Users.csv", "w", encoding="utf-8") as f:
  index = 0
  for user in userlist:
    f.write(str(index)) #Primary key index
    f.write(",")
    f.write(user) #Name attribute
    f.write(",")
    f.write(str(userCountry[index])) #Foreign key to country
    f.write('\n') #New line
    index += 1

#Vacations.csv
with open("Vacations.csv", "w", encoding="utf-8") as f:
  index = 0
  while index < len(vacationUser):
    f.write(str(index)) #Primary key index
    f.write(",")
    f.write(vacationStart[index]) #Start date attribute
    f.write(",")
    f.write(vacationEnd[index]) #End date attribute
    f.write(",")
    f.write(str(vacationUser[index])) #Foreign key to user
    f.write('\n') #New line
    index += 1

#Ratings.csv
with open("Ratings.csv", "w", encoding="utf-8") as f:
  index = 0
  for rating in takenActivityRating:
    f.write(str(takenActivity[index])) #Foreign key to activity
    f.write(",")
    f.write(str(takenActivityVacation[index])) #Foreign key to vacation
    f.write(",")
    f.write(str(rating)) #Rating attribute
    f.write('\n') #New line
    index += 1

print("Files created!")
print("All done c:")