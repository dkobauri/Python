class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}.")


Davit = Person("Davit Kobauri")
Davit.talk()

John = Person("John Dilinger")
John.talk()
