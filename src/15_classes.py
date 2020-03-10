# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

print(LatLon(-44, 33).lat)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    def __str__(self):
        if self.name and self.lat and self.lon:
            return str(self.__class__) + " : " + "\n" f"name: {self.name} \r\nlatitude: {self.lat} \r\nlongitude: {self.lon} "+ "\r\n"
        else:
            return str(self.__class__) + " : " + "\n" + str(self.__dict__) + "\r\n"
# def __repr__(self):
    #     return f"name: {self.__} \r\nlatitude: {self.__} \r\nlongitude: {self.__} "

print(Waypoint("new", -55, 30).name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        super().__init__(name, lat, lon)
    def __str__(self):
        if self.size and self.difficulty:
            return str(self.__class__) + " : " + "\n" f"name: {self.name} \r\nlatitude: {self.lat} \r\nlongitude: {self.lon} \r\nsize: {self.size} \r\ndifficulty: {self.difficulty}"+ "\r\n"
        else:
            return str(self.__class__) + " : " + "\n" + str(self.__dict__) + "\r\n"


print(Geocache("NewTwo", -66, 28, "big", "near impossible").difficulty)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

Catacombs = Waypoint("Catacombs", 41.70505, -121.51521)

print(Catacombs)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint(0, 0, 0)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
Geocache = Geocache("Newberry Views",44.052137, -121.41556, 2, 1.5)
# Print it--also make this print more nicely
print(Geocache)
