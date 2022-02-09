# name = []
# lname = []
#
# for _ in range(5):
#     i_name = input('Please enter name: ')
#     name.append(i_name)
#     i_lname = input('Please enter surname: ')
#     lname.append(i_lname)
#
#
# for i in range(len(name)):
#     print(name[i], lname[i])

d = {}
print(type(d), d)
d = dict()
print(type(d), d)

d = {
    1: 'one',
    2: 'two',
}

print(type(d), d)

lst = [
    (0, 'zero'),
    (1, 'one'),
    (2, 'two'),
]

d = dict(lst)
print(d)

d = dict(
    zero=0,
    one=1,
    two=2
)
print(d)

print(d['one'])

person = {}
# s = person['name']
print(person)
person['name'] = 'Ivan'
print(person)
person['surname'] = 'Ivanov'
person['age'] = 35
person['children'] = ['Pert', 'Olga', 'Mitrofan']
person['pets'] = {'dog': 'Sharik', 'cat': 'Barsik'}
print(person)

print(type(person['children'][1]), person['children'][1])
print(type(person['pets']['cat']), person['pets']['cat'])

# dict.clear()
# person.clear()
# print(person)

# dict.get(key, default)
print(person.get('Name', "No name"))

# dict.keys()
# dict.values()
# dict.items()
print(type(person.keys()), person.keys(), list(person.keys()))
print(type(person.values()), person.values(), list(person.values()))
print(type(person.items()), person.items(), list(person.items()))

for key, value in person.items():
    print(key, value)

# dict.pop(key)
print(person.pop('name'))
print(person)

# dict.popitem()
print(person.popitem())
print(person)
