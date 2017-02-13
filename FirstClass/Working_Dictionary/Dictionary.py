# Dictionary is not sequence,nor indexing but works as key value pairs.
# Dictionary items are in brackets{} in key:values pairs,seperated with "," {"key1":"value1","key2":"value2"}
# indexing will not work on key values
print("*" * 20)

Bag = {'make': 'Gucci', 'style': 'Floral', 'year': 2017}
print(Bag)
print(Bag['make'])

Style = Bag ['style']
print(Style)
Bag['handbag'] = 'stripe'
print(Bag)
print("*#" * 40)





# In this instance,we have an empty variable has been declared,now iam going to insert key:value pairs
Car = {}
Car['one']  = 1
Car['two']  = 2
Car['jeep'] = "Leather"
print(Car)
print("*" * 20)

sum_1 = Car['two'] + 8
print(sum_1)
print(Car)
Car['two'] = Car['two'] + 8
print(Car)
