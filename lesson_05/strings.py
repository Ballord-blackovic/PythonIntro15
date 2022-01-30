s1 = 'Hello\' World!"'
s2 = "Hello' World!\""

"""
\'
\"
"""

s3 = """
;fkwjghsj;erkl'dv\das
"       "
\ewmer'jke\'fk
qwebrgb
            elkrjhgrkhfweoijf
"""
print(s3)

print(chr(0x26bd))
print('\u26bd')     # FF   00
print('\U0001F6A3')
print(chr(9917))

print(ord('⚽'))
print(hex(ord('⚽')))

wave = '~'
boat = '\U0001F6A3'
seagull = '\u033C'
fish = '\U0001F41F'
penguin = '\U0001F427'
wale = '\U0001F40B'
octopus = '\U0001F419'

row = wave * 10 + boat + wave * 15 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 8 + '\n'

sea = row + fish_row + wale_row + penguin_row + octopus_row
print(sea)


"""
        0   1   2   3   4   5
        H   E   L   L   O   !       ===> HELLO!
       -6  -5  -4  -3  -2  -1
"""

s = '>>> Process finished with exit code 0 <<<'
print(s)
print(s[4])
print(s[-5])
# s[4] = '9'

# s[start: stop: step]
print(s[:])

s = '>>> Process finished with exit code 0 <<<'
print(s[9])
print(s[12: 20])
print(s[12: 20: 2])

print(len(s))
print(s[40])
# print(s[41])

print(s[12: 384659834265983])
print(s[-34562352352343: 25])
print(s[-328756328974239: 938476948275093740])
print(s[12:])
print(s[:25])
print(s[::2])
print(s[::-1])

# len()

# str.find(sub, start, end)
# str.rfind(sub, start, end)
s = '>>> Process finished with exit code 0 <<<'
print(s.find('i'))
print(s.find('i', 14))
print(s.find('i', 16))
print(s.find('i', 23))
print(s.find('i', 29))

# str.replace(old, new, count)
s1 = s.replace('i', 'W', 2)
print(s)
print(s1)

# str.count(sub, start, end)
print(s.count('A'))

# str.title()
s1 = s.title()
print(s1)

# str.upper()
# str.lower()
print(s.upper())
print(s.lower())

s = 'Process finished with exit code 0'
print(s)
s = s.lower()
print(s)
# str.capitalize()
print(s.capitalize())

s = 'procEsS finIsheD wiTh eXit cOde 0'
print(s.capitalize())

s = '        >>> Process finished with exit code 0 <<<             '
# str.strip()
print('"' + s.strip().strip('><').strip() + '"')
