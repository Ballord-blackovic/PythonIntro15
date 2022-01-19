"""
Operators
"""

"""
+           3 + 4, 5.6 + 4,  'Hello' + ' World' ==> 'Hello World'   int + int => int flat + int => float str + str = str
-           4 - 5, 4.5 - 6.2                                        int - int = int float - int = float
*           5 * 6, 6.3 * 2  'Hello ' * 3 ==> 'Hello Hello Hello'    int * int = int float * int = float str * int = str
**          3 ** 4, 2 ** 3 ** 4
/           10 / 4 => 2.5,                                          int / int = float int / float = float
//          10 // 4 => 2                                            int // int = int int // float = float
%           10 % 4 => 2,  3 % 2352352345235243453 => 3,  1235 % 1000 => 235
"""

"""
>           3 > 5
<
>=
<=
!=
==
"""

"""
=           A = B
"""

"""
a = 1       a = a + 1       a = a + 8       a += 1, a += 8
+           +=
*           *=
/           /=
//          //=
%           %=
**          **=
>>          >>=
<<          <<=
&           &=
|           |=
^           ^=
"""

"""
and         И           A and B
or          ИЛИ         A or B
not         НЕ          not A


    A       B      and       or      not A
  True    True    True     True      False
  True    False   False    True      False
  False   True    False    True      True
  False   False   False    False     True

    False and X  ==> False
    
    True or X  ==> True
    
    4 and 5
"""

"""
&       битовое И                       A & B
|       битовое ИЛИ                     A | B
^       битовое Исключающее ИЛИ         A ^ B
~       битовое НЕ                        ~ A

  4 & 5
  
    A       B      ^
  True    True    False
  True    False   True
  False   True    True
  False   False   False
"""
"""
  4     ==>     0100    &       A
  5     ==>     0101            B
                0100 
                
  ~ 4   ==>    ~ 0100   ==>     1011
"""

"""
>>          A >> B
<<          A << B

            4 >> 2      ===>   0100 >> 2  ==>   0001 ==> 1
            8 << 3      ===>   00001000 << 3  ==>  01000000 ==> 64
"""

a = 223         # 11011110      &
                # 00000010
mask = 1


print(a & mask)
mask <<= 1

print(a & mask)
mask <<= 1

print(a & mask)
mask <<= 1

print(a & mask)


"""
+       + A 
-       - A

5 ==> -5

5 + (3 * 6) / 3
"""
