# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv
import textwrap


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __repr__(self):
        return f"({self.name} is located at coordinates {self.lat}, {self.lon}."
# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
# import csv
# >>> with open('names.csv', newline='') as csvfile:
# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:
# ...         print(row['first_name'], row['last_name'])
# ...
# Eric Idle
# John Cleese

# >>> print(row)
# OrderedDict([('first_name', 'John'), ('last_name', 'Cleese')])


cities = []


def cityreader(cities=[]):
    with open('cities.csv', newline='') as coolcsv:
        citydictreader = csv.DictReader(coolcsv)
        for row in citydictreader:
                        # wait, name is not included? so why did i put in a thing called name up in the City object? im so confused
            cities.append(City(row['city'], row['lat'], row['lng']))
        # lol i indented too far to the right for the return, only got one entry back, its fixed now
        return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
lat1 = input("Please input the latitude of the first location. ---->>>")
lon1 = input("Awesome, now input the longitude of the first location. ----->>>")
lat2 = input("Please input the latitude of the second location. ---->>>")
lon2 = input(
    "Awesome, now input the longitude of the second location. ----->>>")

# yikes, maybe i should turn this into a dictionary and clean this up. will ask.
lat1 = float(lat1)
lat2 = float(lat2)
lon1 = float(lon1)
lon2 = float(lon2)


# might be better to use split, like so:
# cmd = input("Hello, please input the two locations in the following manner: lat1,lon1,lat2,lon2: ").split(",")
# This splits the input into a list wherever there is a comma

print(
    f'Great, the latitude and logitude of the first location is {lat1}, {lon1}, and the second location is at {lat2}, {lon2}')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
    within = []

    # to normalize the coordinates, you might have to mulitply all the coordinates by negative 1.
    for city in cities:
        if lat1 > city.lat > lat2:
            if lon1 > city.lon > lon2:
                within.append(city)
            else:
                break
        else:
            break
    return within

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

# Bondor's solution: seems like it naturalizes the coordinates so it passes regardless of the orientation.
    # if lat1 < lat2:
    #     lat1, lat2 = lat2, lat1
    # if lon1 < lon2:
    #     lon1, lon2 = lon2, lon1

    # for c in cities:
    #     if c.lat < lat1 and c.lat > lat2 and c.lon < lon1 and c.lon > lon2:
    #         within.append(c)

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#     within = []

#     lat1, lon1 = float(lat1), float(lon1)
#     lat2, lon2 = float(lat2), float(lon2)

#     # Normalizex

#     if lat2 < lat1:
#         lat1, lat2 = lat2, lat1  # Swap

#     if lon2 < lon1:
#         lon1, lon2 = lon2, lon1  # Swap

#     # Filter

#     for c in cities:
#         if c.lat >= lat1 and c.lat <= lat2 and c.lon >= lon1 and c.lon <= lon2:
#             within.append(c)

#     return within
