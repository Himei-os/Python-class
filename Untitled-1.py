class Giraffe:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def swim(self, can_swim=False):
        if can_swim:
            return f'{self.name} can swim.'
        else:
            return f'{self.name} can NOT swim.'

    def sing(self, can_sing=False):
        if can_sing:
            return f'{self.name} can sing.'
        else:
            return f'{self.name} can NOT sing.'

    def dance(self, can_dance=False):
        if can_dance:
            return f'{self.name} can dance.'
        else:
            return f'{self.name} can NOT dance.'





giraffe = Giraffe('Giraffe', 8, 'Yellow-Brown')


print(giraffe.swim())

print(giraffe.sing(True))

print(giraffe.dance(True))