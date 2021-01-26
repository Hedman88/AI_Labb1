
class WorkState:
    def Execute(self, inhabitant):
        inhabitant.hunger -= 1
        inhabitant.thirst -= 1
        inhabitant.energy -= 1
        inhabitant.happiness -= 1
        inhabitant.money += 1
