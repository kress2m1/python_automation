"""
Accessing characters in a String
"""

"""
Here, we will access the first character of the index"""
sample_char = "nyc"[0]
print("The first character in \"nyc\" is: " + sample_char)
extend_char = sample_char[0]
print("I've extended object \"sample_char\" "
      "and the second character is: " + extend_char)
print()

"""
The following are methods used to supplement Strings
"""

string_sample = "This is a Mixed case String"
print(string_sample)
print("The length of the String is: ", str(len(string_sample)))
print("lowercase: ", string_sample.lower())
print("UPPERCASE: ", string_sample.upper())
print(string_sample, str(2), str(4), "I've added 2 and 4 to the String")
