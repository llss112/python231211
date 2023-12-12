#Person.py

class Person:
    def __init__(self):
        self.name="default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1=Person()
p2=Person()

p1.name="강감찬"
p1.print()
p2.print()


Person.title="new title"

print(p1.title)
print(p2.title)
print(Person.title)
# 클래스에 다 들어가서 title치면 다 나온다.
