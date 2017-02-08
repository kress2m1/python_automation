# Dictionary items are in brackets{} in key:values pairs,seperated with "," {"k1":"v1","k2":"v2"}
print("*" * 20)

Bag = {'make': 'Gucci', 'style': 'Floral', 'year': 2017}
print(Bag)

d = {}

Style = Bag ['style']

print(Bag['make'])
print(Style)

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)
