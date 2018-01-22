# DjangoGirls code for 1.12.18

# recap of class construction, with and without __init__() methods

# without:

class classname:
    pass

firstObject = classname()

firstObject.age = 37
firstObject.height = 1.73

print(firstObject.age)
print(firstObject.height)


# with:

class class2name:

    def __init__(self, age, height):
        self.age = age
        self.height = height

    def ageAndHeight(self):
        print(self.age, "years old,", self.height, "cm.")

secondObject = class2name(38, 1.74)
secondObject.ageAndHeight()
