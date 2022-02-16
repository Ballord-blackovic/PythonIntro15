s = 'Number: {} - {} - {}'
s1 = s.format(3, 7, 9)

print(s1)

# { [field_name] [!modifier] [:specification]  }
# [fill] align [sign] [width] [.precision] [type]

# < > = ^
# 00000-45
# -0000045

# + - ' '
# -   56

# d, c, e, E, f, F

coord = (4, 5)
print('X: {0[0]}, Y: {0[1]}'.format(coord))

print("'{:<30}'".format('left'))
print("'{:>30}'".format('right'))
print("'{:^30}'".format('center'))
print("'{:*^30}'".format(' center '))

print('"{:^+23.2f}"  "{:+f}"'.format(3.14, -3.14))
print('"{:^ 23.2f}"  "{: 23.2f}"'.format(3.14, -3.14))

print('int: {num}   hex: {num:x}   oct: {num:o}   bin: {num:b}'.format(num=123456))

alfa = 9
beta = 23

s = f'Alfa: {alfa}, Beta: {beta}'
print(s)

r = r'Hello \n World!'
print(r)
