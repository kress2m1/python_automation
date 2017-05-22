"""
Examples of more String methods in python
"""

alphabet = "1abc2abc3abc4abc5abc6abc7abc8abc"
print("The value of variable 'alphabet' is: ", alphabet)
print("Replace \'abc\' with \'ABC\'")
print("The value of variable 'alphabet' is now: ", alphabet.replace("abc", "ABC", 3))
print("The value of variable 'alphabet' is now: ", alphabet.replace("abc", "ABC"))

"""
Print only the 1st to the 7th characters
"""
alphabet_sub = alphabet[0:13]
print("The value of alphabet_sub is: ", alphabet_sub)

"""
Print the 1st to the 13th character, skipping every 4th character
"""
alphabet_step = alphabet[0:13:4]
print("The value of alphabet_step is now: ", alphabet_step)

"""
The whole string is printed here as the code assumes that ithas to start from the beginning and up to the end
"""
alphabet_whole = alphabet[:]
print("The whole alphabet string is printed in UPPERCASE: ", alphabet_whole.upper())
print("*************")
a = "test"[1:2]
print(a)
