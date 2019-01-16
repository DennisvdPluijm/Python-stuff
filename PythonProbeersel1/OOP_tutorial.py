class Dog:
    def __init__(self, name, age):  # required init method, initializer, with at least 'self' argument
        self.name = name  # required attributes
        self.age = age

    def bark(self):  # this is a method
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy  # optional attribute, not required
        buddy.buddy = self  # reciprocal relationship


# instantiate an object, of class Dog
ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

print(ozzy)  # gives object info
# print(ozzy.name)
# print(ozzy.age)

ozzy.doginfo()
skippy.doginfo()
filou.doginfo()

ozzy.bark()

print(ozzy.age)
print("It's Ozzy's birthday!")
ozzy.birthday()
print(ozzy.age)

ozzy.setBuddy(filou)
print(ozzy.buddy.name)
print(ozzy.buddy.doginfo())

