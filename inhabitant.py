import fsm
class Inhabitant:
    money = 0.0
    food = 0.0
    water = 0.0
    hunger = 100.0
    thirst = 100.0
    energy = 100.0
    happiness = 100.0
    def __init__(self, ID, name, state):
        self.ID = ID
        self.name = name
        self.state = state

    def Update(self):
        if(self.energy <= 0):
            self.ChangeState(fsm.SleepState())
        if(self.hunger <= 0 or self.thirst <= 0 or self.happiness <= 0):
            self.ChangeState(fsm.DeadState())
        else:
            self.PrintStats()
            
        self.state.Execute(self)

    def CheckNeeds(self):
        baseStatThreshold = 30
        self.ChangeState(fsm.WorkAtOfficeState())
        if(self.money > baseStatThreshold and (self.food < 100 or self.water < 100)):
            self.ChangeState(fsm.ShoppingState())
        if(self.hunger < baseStatThreshold):
            if(self.food > 0):
                self.ChangeState(fsm.EatState())
            elif(self.money >= 5):
                self.ChangeState(fsm.ShoppingState())
            else:
                self.ChangeState(fsm.WorkAtOfficeState())

        if(self.thirst < baseStatThreshold and self.thirst < self.hunger*1.5):
            if(self.water > 0):
                self.ChangeState(fsm.DrinkState())
            elif(self.money >= 5):
                self.ChangeState(fsm.ShoppingState())
            else:
                self.ChangeState(fsm.WorkAtOfficeState())

        if(self.energy < baseStatThreshold and self.energy < self.hunger and self.energy < self.thirst):
            self.ChangeState(fsm.SleepState())

        if(self.happiness < baseStatThreshold and self.happiness < self.hunger and self.happiness < self.thirst and self.happiness < self.energy):
            self.ChangeState(fsm.SocialState())

    def ChangeState(self, newState):
        self.state = newState

    def AddStats(self, money, hunger, thirst, energy, happiness):
        self.money += money
        self.hunger += hunger
        self.thirst += thirst
        self.energy += energy
        self.happiness += happiness

    def AddItems(self, food, water):
        self.food += food
        self.water += water

    def PrintStats(self):
        print(self.name, "_", self.ID, "_", self.state)
        print("Money: ", self.money)
        print("Hunger: ", self.hunger)
        print("Food: ", self.food)
        print("Thirst: ", self.thirst)
        print("Water: ", self.water)
        print("Energy: ", self.energy)
        print("Happiness: ", self.happiness)

    def SendMessage(self, rcvrID, content):
        msg = Message(self.ID, rcvrID, content)
        
    def RcvMessage(self, msg):
        if(msg.content == "Hello there"):
            self.SendMessage(msg.senderID, "Obi Wan")

class Message:
    def __init__(self, senderID, rcvrID, content):
        self.senderID = senderID
        self.content = content
