#create a mapping of state to abbreviation

states = {
    "Oregon" : "OR",
    "Florida" : "FL",
    "California" : "CA",
    "New York" : "NY",
    "Michigan" : "MI"
    }

#create a basic set of states and some cities in them

cities = {
    "CA" : "San Fransico",
    "MI" : "Detroit",
    "FL" : "Jacksonville"
    }

print(cities)

#add some more cities

cities["NY"] = "New York"
cities["OR"] = "Portland"

print(cities)

#print out some cities
print("_" * 10)
print("NY State has: ", cities["NY"])

#print some state
print("_" * 10)
print("Michigan's abbreviation is: ",states["Michigan"])
print("Florida's abbreviation is: ",states["Florida"])

#do it by using the state then city dict
print("_" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

#print every states abbrevation
print("_" * 10)
for state, abbrevation in states.items(): #items() returns a list of dict's (key, value) tuple pairs
    print("{} is abbreviation for {}".format(state, abbrevation) )

#print every city in state
print("_" * 10)
for abbrevation, city in cities.items():
    print("{} has the city {}".format(abbrevation, city))

#now do both at the same time
print("_" * 10)
for state, abbrevation in states.items():
    print("{} state is abbreviated {} and has city {}".format(state, abbrevation, cities[abbrevation]))

print("_" * 10)
#safely get an abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get("TX", "Does not exist")
print("The city for the state 'TX' is: {}".format(city))

#print all cities
print("_" * 10)
for city in states:
    print("City: ", cities[states[city]])

#print abbreviations
print("_" * 10)
for state, abbreviations in states.items():
    print(abbreviations)
    




