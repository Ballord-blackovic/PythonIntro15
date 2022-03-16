"""
 F(2 ^ 5) = 2 * 2 * 2 * 2 * 2
 f(2 ^ 5) => 2 * f(2 ^ 4) => 2 * f(2 ^ 3) => 2 * f(2 ^ 2) => 2 * f(2 ^ 1) => 2 * f(2, 0)
     32   <= 2 *    16    <=  2 *    8    <= 2 *     4    <= 2 *     2    <= 2 *    1
"""


def i_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1
    return res


# f(2 ^ 3) => 2 * f(2 ^ 2) => 2 * f(2 ^ 1) => 2 * f(2, 0)
def r_pow(num, exp):
    if exp == 0:
        return 1
    return num * r_pow(num, exp-1)


print(i_pow(2, 5))
print(r_pow(2, 5))


"""
    5! = 5 * 4 * 3 * 2 * 1      => 120
    5! = 5 * 4! => 4 * 3! => 3 * 2! => 2 * 1! => 1
  120 <= 5 * 24 <= 4 * 6  <= 3 * 2  <= 2 * 1
"""


def i_fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


def r_fact(num):
    if num == 1:
        return 1

    return num * r_fact(num-1)


print(i_fact(5))
print(r_fact(5))


"""
A() => A()

A() => B() => C() => A()

A(n) => A(n+1) + A(n-3)

0, 1, 2, 3, 4, 5, 6, 7,  8,  9
0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
   x  y
"""


def i_fib(n):
    x = 0
    y = 1
    while n > 0:
        res = x + y
        x = y
        y = res
        n -= 1
    return x


def r_fib(n):
    # if 0 == n or n == 1:
    #     return n
    #
    # return r_fib(n-1) + r_fib(n-2)
    return n if 0 == n or n == 1 else r_fib(n-1) + r_fib(n-2)


print(i_fib(9))
print(r_fib(9))
