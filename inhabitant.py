from fsm import WorkState
class Inhabitant:
    money = 0.0
    hunger = 100.0
    food = 0.0
    thirst = 100.0
    water = 0.0
    energy = 100.0
    happiness = 100.0
    def __init__(self, ID, name, state):
        self.ID = ID
        self.name = name
        self.state = state

    def Update(self):
        self.state.Execute(self)

    def ChangeState(self, newState):
        self.state = newState

    def PrintStats(self):
        print(self.name, " ", self.ID, " ", self.state)
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
