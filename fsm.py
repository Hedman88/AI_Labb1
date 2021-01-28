
class WorkAtQuarryState:
    def Execute(self, inhabitant):
        inhabitant.AddStats(+2, -2, -3, -2, -1)
        inhabitant.CheckNeeds()

class WorkAtOfficeState:
    def Execute(self, inhabitant):
        inhabitant.AddStats(+3, -1, -2, -1, -3)
        inhabitant.CheckNeeds()

class ShoppingState:
    def Execute(self, inhabitant):
        inhabitant.AddStats(-5, -1, -2, -1, +1)
        inhabitant.AddItems(+3, +3)
        inhabitant.CheckNeeds()

class SleepState:
    def Execute(self, inhabitant):
        if(inhabitant.energy > 100-3 or inhabitant.thirst < 15 or inhabitant.hunger < 15):
            inhabitant.CheckNeeds()
        else:
            inhabitant.AddStats(0, -0.5, -1, +3, +0.5)
        
class EatState:
    def Execute(self, inhabitant):
        if(inhabitant.food <= 0 or inhabitant.hunger > 100-3):
            inhabitant.ChangeState(DrinkState())
        else:
            inhabitant.AddStats(0, +3, -0.5, +1, +0.5)
            inhabitant.AddItems(-1, 0)

class DrinkState:
    def Execute(self, inhabitant):
        if(inhabitant.water <= 0 or inhabitant.thirst >= 50):
            inhabitant.CheckNeeds()
        else:
            inhabitant.AddStats(0, 0, +6, +1, +0.5)
            inhabitant.AddItems(0, -1)

class SocialState:
    def Execute(self, inhabitant):
        if(inhabitant.happiness >= 50):
            inhabitant.CheckNeeds()
        else:
            inhabitant.AddStats(0, -1, -1, -1, +3)

class DeadState:
    def Execute(self, inhabitant):
        print(inhabitant.name, "ID:", inhabitant.ID, "is dead!!!!!")
        if(inhabitant.hunger <= 0):
            print("Died to starvation")
        if(inhabitant.thirst <= 0):
            print("Died to dehydration")
        if(inhabitant.happiness <= 0):
            print("Died to suicide")
