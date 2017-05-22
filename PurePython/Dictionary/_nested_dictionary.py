"""
The following will look at a nested dictionary
"""

# Create a nested dictionary of two different cars
cars = {"BMW": {"model": "550i", "year": 2017}, "BENZ": {"model": "35E", "year": 2016}}
"""
In the sample above, the "model" and "year" are the values of the keys BMW and BENZ
They are also dictionaries in their own right
"""
print("The list of cars and their values are:", cars)
print("--" * 10)
print("The values for the BMW are:", cars["BMW"])
print("--" * 10)
print("The values for the BENZ are:", cars["BENZ"])
print("--" * 10)
print("The value for the BENZ model is:", cars["BENZ"]["model"])
print("--" * 10)

# Change the value for the BENZ model
cars["BENZ"]["model"] = "65v8i"
# Assign the BENZ model to a suitable variable name
BENZ_model = cars["BENZ"]["model"]
print("The new BENZ model is:", BENZ_model)
print("--" * 10)

# Assign the keys to suitable variable names
BMW = cars["BMW"]
BENZ = cars["BENZ"]
print("The values for the BMW are:", BMW)
print("The values for the Benz are:", BENZ)
print("--" * 10)

d = {"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}
print(d)
print(d["key1"][2])
