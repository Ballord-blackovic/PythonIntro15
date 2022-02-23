# file_object = open(filename, mode, encoding)

"""
mode

r       read        (default)
w       write
x       exclusive
a       append

t       text        (default)
b       binary

+

rb+

wt
rt
wt+
"""

"""
end of lines

windows     \r\n
linux       \n
mac         \r

"""

# file = open('test.txt', 'wt', encoding='utf-8')
# file.write('Process finished with exit code 0\n')
# file.write('124323523531\n')
# file.write('Привет Мир!\n')
# file.close()
#
# file = open('test.txt', 'rt', encoding='utf-8')
# text = file.read()
# file.close()
# print(text)

from pprint import pprint as pp

lst = [
    'Максимальное напряжение, B              250',
    'Максимальный ток, А                     6',
    'Тип рабочего тока                       переменный',
    'Высота педали, мм                       43.5',
    'Толщина педали, мм                      18',
    'Количество контактов (без реверса)      6'
]

pp(lst)
# print(lst)

file = open('example_file.txt', 'w', encoding='utf-8')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()
print()

# read all
print()
file = open('example_file.txt', encoding='utf-8')
lst = file.read()
file.close()
pp(lst)
print()

# read all
print()
lst = []
file = open('example_file.txt', encoding='utf-8')
lst = file.readlines()
file.close()
pp(lst)
pp(list(map(lambda x: x.strip('\n'), lst)))
print()

# read by 40 symbols
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
while True:
    line = file.readline(40)
    if line != '':
        lst.append(line.strip('\n'))
    else:
        break
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
for line in file.readlines():
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt', encoding='utf-8')
for line in file:
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)


src = open('istockphoto.jpg', 'rb')
dst = open('istockphoto_copy.jpg', 'wb')
buffer = 100
while True:
    data = src.read(buffer)
    if data:
        dst.write(data)
    else:
        break
src.close()
dst.close()
