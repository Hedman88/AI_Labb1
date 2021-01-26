
class WorkState:
    def Execute(self, inhabitant):
        inhabitant.hunger -= 1
        inhabitant.thirst -= 1
        inhabitant.energy -= 1
        inhabitant.happiness -= 1
        inhabitant.money += 2

class SleepState:
    def Execute(self, inhabitant):
        inhabitant.hunger -= 1
        inhabitant.thirst -= 1
        inhabitant.energy += 3
        inhabitant.happiness += 0.5
        
class EatState:
    def Execute(self, inhabitant):
        inhabitant.hunger += 3
        inhabitant.thirst -= 0.5
        inhabitant.energy += 1
        inhabitant.happiness += 0.5

class DrinkState:
    def Execute(self, inhabitant):
        inhabitant.hunger -= 0
        inhabitant.thirst += 6
        inhabitant.energy += 1
        inhabitant.happiness += 0.5

class SocializingState:
    def Execute(self, inhabitant):
        inhabitant.hunger -= 1
        inhabitant.thirst -= 1
        inhabitant.energy -= 1
        inhabitant.happiness += 3
