"""
This is a datatype used to store more than one value in one variable name,
in terms of 'key-value-pairs' (KVP).
Dictionary items  are in brackets {} in "key":"value" pairs, and are
separated with a comma. ie: {"k1":"v1", "k2":"v2"}
KVP are not sequenced, nor are they indexed, rather, they are mapped to each other
"""
man = {"age": 24, "name": "Andre", "sex": "male", "height": "5ft 8inc"}
print("The 'man' dictionary contains", man)
# Print the 'age' value
print("The age of the man is:", man["age"])
# Print the name value
print("The name of the man is:", man["name"])

print("--" * 10)
# The keys can be stored inside a variable, making easier to call their variables
age = man["age"]
print("My age is:", age)
name = man["name"]
print("My name is:", name)
sex = man["sex"]
print("My sex is:", sex)
height = man["height"]
print("My height is:", height)
print("--" * 10)

# Let's define an empty dictionary
empty_dictionary = {}
print("The 'empty_dictionary' contains", empty_dictionary)
# Let's input the first KVP into the empty dictionary
empty_dictionary[1] = "ant"
print(empty_dictionary)
print("--" * 10)
# Enter the second KVP
empty_dictionary[2] = "ball"
print(empty_dictionary)
print("--" * 10)
# Enter the third KVP
empty_dictionary["Cat"] = "animal"
print(empty_dictionary)
print("--" * 10)
# Enter the fourth KVP
empty_dictionary[4] = 4
print(empty_dictionary)
print("--" * 10)
# Multiply the fourth KVP by 4
sum_four = empty_dictionary[4] * 4
print(sum_four)
print("--" * 10)
# Substitute the previous value for the fourth entry with the new value
empty_dictionary[4] = sum_four
print(empty_dictionary)
