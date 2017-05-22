"""
The List methods that come built in with python will be explored here
"""

name = ["Andre", "Uyi", "Thelma", "Osato", "Andre"]
print("The current list contains:", name)
print("--" * 10)

# Get the length of the method list
print("The length of the name list is:", len(name))
print("--" * 10)

# Extend the length of the current list by adding a new entry at the end
name.append("Iyore")
print("The length of the name list is now:", len(name), ", and it now contains:", name)
print("--" * 10)

# Insert a new entry into the list at a specific index
name_insert = name.insert(2, "Ame")
print("I've added \"Ame\" at index 2")
print("The list now displays as", name)
print("--" * 10)

# Find the index of a particular item inside the list
ame_index = name.index("Ame")
print("\"Ame\" is listed at index", ame_index)
print("--" * 10)

# Remove an item from the list. Default behaviour when no parameters
list_amend = name.pop()  # Where no parameters are given, the default is to remove the last item in the list
print("Remove the last item from the current list")
print(list_amend)
print("The list is now", name)
print("--" * 10)

# Remove a specific item from the list
name.remove("Uyi")
print("\"Uyi\" has been removed from the list and the list now displays;", name)
print("--" * 10)

"""
Slicing can also be performed on a list
"""
print("We will be demonstrating slicing on the list here")
print("The current list is:", name)
sliced_name = name[2:]
print("The names are now displayed, stating from the 2nd index \"Thelma\":", sliced_name)
print("The last name will be removed from the list")
last_name = name[:3]
print("\"Osato\" has been removed from the list:", last_name)
print("--" * 10)

"""
The list can be sorted
"""
print("Adding a single entry to the name list...")
name.insert(2, "James")
print("The name list as default", name)
print("Adding multiple entries to the name list...")
name.extend(["Brown", "Wale", "Dare", "Thomas", "Andre"])
print("The name list is now:", name)
name.sort() # This will sort it alphabetically
print("The name has been sorted alphabetically:", name)
print("The size of the list is now:", len(name))
# Check how many times the name Andre appears in the list and print it out
name_count = name.count("Andre")
if name_count <= 1:
    print("Andre appears", name_count, "time in the name list")
else:
    print("Andre appears", name_count, "times in the name list")


