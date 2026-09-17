class Djur:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Hund(Djur):
    def make_sound(self):
        print("hunden låter woof")
class katt(Djur):
    def make_sound(self):
        print("katten låter meow")

class ko(Djur):
    def make_sound(self):
        print("ko låter mooo")