class fordon:
    def __init__(self, fordontyp, regnr):
        self.fordontyp = fordontyp
        self.regnr = regnr

class lastbil(fordon):
    def __init__(self, fordontyp, regnr, maxvikt):
        super().__init__(fordontyp, regnr)
        self.maxvikt = maxvikt
    
      def honka(self):
        print("Honk honk!")


class motorcykel(fordon):
    def wheelie(self):
        print("Doing a wheelie!")
    def senastebesiktning(self):
        print("Senaste besiktning: 2027-01-01")