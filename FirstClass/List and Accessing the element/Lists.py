dresses = ["coast","next","Primark"]
print(dresses)
print("*#"  * 20)
print(dresses[0])

num_list =[1,2,3]
sum_num = num_list[1] + num_list[2]
print(sum_num)

More_dresses = ["Tmlewin","tHOMAS PINK"]
print(More_dresses[1])

More_dresses[1] ="coast"
print(More_dresses[1])
print(More_dresses)


#Built-in methods to help manipulating a list

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort()

print(cars)