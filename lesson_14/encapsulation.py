# Инкапсуляция
from pprint import pprint

"""
- public
- private
- protected
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu
        self._memory = memory
        self.hdd = hdd


c = Computer(2300, 16000, 2000)
pprint(dir(c))
print(c._memory)
print(c._Computer__cpu)
print(c.hdd)
