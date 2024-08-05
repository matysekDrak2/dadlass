class Person:
    pass

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print(self):
        print(self.name, self.age, self.gender)

    def isOlderThan(self, otherPerson: Person) -> bool:
        if self.age > otherPerson.age:
            return True
        return False

if __name__ == "__main__":
    clovek = Person("dadla", 17, "female")
    clovek1 = Person("dadla2", 11, "male")

    print(clovek1.isOlderThan(clovek))
int