# Replacing character in strings

a = "Two jolly friends,always jolly"

print(a.replace("jolly", "good", 2))

login = "Enter valid username with valid Password"

# print(login.replace("valid","invalid",1))

b = "1abc2abc3abc"

# sub-string
# starting index is inclusive  and ending index is exclusive
print("*******************************")
sub = login
print(sub)
sub = login[0:6]
print(sub)
sub = login[:]
print(sub)
step = login[1:14:7]
print(step)
step2 = login[1:14]
print(step2)
print("*******************************")
print(sub)
print(step)

# Slicing/indexing

a = "This is a string"
a[1:]
print(a)


