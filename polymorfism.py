#superklass
class player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

#Subklass 
class admin(player):
    def banplayer(self,name):
        self.bancount = bancount
        super().__init__(name, level)

    def banplayer(self, name):
        print(f"player {name} was banned!")
        self.bancount +=1
    
p1 = player("steve", 23)
p2 = admin(0, "Alex", 9696)
p2.bancount = 0

p2.banplayer("steve")

