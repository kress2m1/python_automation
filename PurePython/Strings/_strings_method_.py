"""
The following are examples on how to use Strings in python
"""

text = "1. This is sample string"
print(text)
print()

"""
One way to handle quotes in a String using alternate 'quote' characters
"""
escape = "2. I want 'single quotes' to be displayed in the String "
print(escape)
print()

"""
Another way to handle quotes in a String using 'escape characters'
"""
backslash = "3. I also want \"double quotes\" to be displayed in the String"
print(backslash)
print()

"""
Display a break in a String
"""
broken = "4. Display a broken\n\
string over two lines"
print(broken)
print()

"""
Display a long String with a break in it
"""
not_broken = "5. This String does not have" \
             "a break in the middle, " \
             "even if the code shows it over 3 lines"
print(not_broken)
