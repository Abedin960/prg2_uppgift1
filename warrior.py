#superklass
class player:
    def attack(self):
        print("player is attacking!")
    
class warrior(player):
    def attack(self):
        print("warrior is attacking with a sword!")
class mage(player):
    def attack(self):
        print("mage is attacking with a spell!")

player =[
    player(),
    warrior(),
    mage()
]

for player in player:
    player.attack()
