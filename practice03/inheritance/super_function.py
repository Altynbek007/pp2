class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)


c = Child("Anna")
print(c.name)