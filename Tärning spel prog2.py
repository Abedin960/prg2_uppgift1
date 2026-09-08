import random
from random import randint

class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.poäng = 0
        

    def kasta(self):
        return random.randint(1, 6)

    def vinn_runda(self):
        self.poäng +=1

Spelare1 = Spelare("Maria")
Spelare2 = Spelare("Johan")


    
while True:
    kast1 = Spelare1.kasta()
    kast2 = Spelare2.kasta()

    print(f"{Spelare1.namn} kastar: {kast1}")
    print(f"{Spelare2.namn} kastar: {kast2}")

    if kast1 > kast2:
        Spelare1.vinn_runda()
        print(f"{Spelare1.namn} vinner rundan!")
        print()
    elif kast2 > kast1:
        Spelare2.vinn_runda()
        print(f"{Spelare2.namn} vinner rundan!")
        print()
    else:
        print("Oavgjort!")
        print()

    if Spelare1.poäng == 5:
        print(f"{Spelare1.namn} vann")
        break
    if Spelare2.poäng == 5:
        print(f"{Spelare2.namn} vann")
        break