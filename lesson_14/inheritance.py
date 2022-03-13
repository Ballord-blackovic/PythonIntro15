# Наследование

class WaterBird:
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim')

    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin is ready')

    def where_is_live(self):
        print('South Pole')

    def run(self):
        print('Can running')

    def voice(self):
        print('Pi-pi-pi')


class Duck(WaterBird):
    # def __init__(self, name):
    #     super().__init__(name)
    #     print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def flying(self):
        print('Can fly')

    def voice(self):
        print('Kra-kra-kra')


p = Penguin('Ping')
p.run()
p.swim()
p.voice()
p.where_is_live()
print('========================')
d = Duck('Donald Dug')
d.flying()
d.swim()
d.voice()
d.where_is_live()
