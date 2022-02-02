from random import randint
from random import random
from random import randrange
from random import uniform

# randint(start, stop)      1 - 100
for _ in range(25):
    print(randint(-50, 50), end=' ')
print()

# random()      0 - 1
for _ in range(15):
    print(round(random(), 2), end=' ')
print()

# randrange(start, stop, step)  range(1, 10, 2)  1, 2, 3, 4, 5, 6, 7 ,8, 9  => 1, 3, 5, 7, 9
#                           randrange(1, 10, 2)  6, 4, 8, 3, 7, 9, 2, 1, 5  => 7, 5, 9, 7, 1
for _ in range(25):
    print(randrange(1, 10, 2), end=' ')
print()

# uniform(start, stop)
for _ in range(15):
    print(round(uniform(1, 10), 2), end=' ')
print()
