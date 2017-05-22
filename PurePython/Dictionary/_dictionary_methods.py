"""
The following are samples of methods used to compliment the dictionary class
"""

car = {"make": "Toyota", "model": "Supra", "year": 2017}
cars = {"BMW": {"make": "Evolution", "model": "E50i", "year": 2017}, "LEXUS": {"make": "Legend",
                                                                               "model": "Saturn2", "year": 2015}}
# The 'keys()' method lists all the keys in the dictionary
print("The keys for both the car and cars dictionary are:")
print(car.keys())
print(cars.keys())
print("--" * 10)

# The 'values()' method lists all the values in the dictionary
print("The values for both the car and cars dictionary are:")
print(car.values())
print(cars.values())
print("--" * 10)

# The 'items()' method displays all the items in a 'tupple' view
print(car.items())
print(cars.items())
print("--" * 10)

# A dictionary can be copied using the '.copy()' method
car_copy = car.copy()
print("This is the copied car dictionary", car_copy)
cars_copy = cars.copy()
print("This is the copied cars dictionary", cars_copy)
print("--" * 10)

# A KVP can be popped, excluded, from a dictionary and won't be returned when next the dictionary is called
print("The full car dictionary is:", car)
car.pop("make")
print("The car dictionary after 'make' is popped:", car)
print("--" * 10)

# A dictionary can be cleared using the '.clear()' method
car.clear()
print("The car dictionary is cleared", car)
cars.clear()
print("The cars dictionary is cleared", cars)
print("--" * 10)

d = {"airport code": "city"}
print(d)