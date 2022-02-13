a = 9


def func():
    global a
    a = 15
    print(a)


# a += 1
print(a)        # 9
func()          # 15
print(a)        # 9

