class fu:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class zi(fu):

    def __init__(self,six):
        super(zi, self).__init__(six)

c = zi('a')

# print(c.name)
