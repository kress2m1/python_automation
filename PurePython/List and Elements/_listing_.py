"""
A list is used to store more than one value in a variable name
List items are in brackets, are indexed, and are separated by a comma ["item1", "item2", "item3"]
"""

cars = ["BMW", "Volvo", "Passat"]
print("The list of cars are:", cars)
print("The car at the 2nd index is a: " + cars[2])
print("--" * 10)

"""
This is an example of an empty list
"""
empty_list = []
print("This is an empty list", empty_list)
print("--" * 10)

"""
Some math solutions using a list
"""
int_list = [1, 2, 3]
zero = int_list[0]
one = int_list[1]
two = int_list[2]
add_sum = two * one
print("%s multiplied by %s = %s" % (two, one, add_sum))
print("--" * 10)

duo_list = [22, 44, 77]
first = duo_list[0]
second = duo_list[1]
third = duo_list[2]
sub_mult_sum = third - first * second
print("%s subtracted from %s and multiplied by %s is %s" % (third, first, second, sub_mult_sum))

"""
List items can be replaced
"""
animals = ["Dog", "Lion", "Tiger", "Goat"]
print("The list of animals are", animals)
print("The 2nd animal in the list is a:", animals[2])
animals[2] = "Elephant"
print("The 2nd animal in the list is now an:", animals[2])
print("The list of animals are now:", animals)
print("--" * 10)

