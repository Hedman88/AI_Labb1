import fsm
import messagehandler as mh
import inhabitanthandler as ih
from enum import Enum
class Inhabitant:
    money = 0.0
    food = 0.0
    water = 0.0
    hunger = 100.0
    thirst = 100.0
    energy = 100.0
    happiness = 100.0
    maxStat = 100.0
    def __init__(self, ID, name, workPlace):
        self.ID = ID
        self.name = name
        self.defaultWorkState = workPlace
        self.state = self.defaultWorkState

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
        tempState = fsm.WorkState()
        if(self.money > baseStatThreshold and (self.food < 100 or self.water < 100)):
            tempState = fsm.ShoppingState()
        if(self.hunger < baseStatThreshold):
            if(self.food > 0):
                tempState = fsm.EatState()
            elif(self.money >= 5):
                tempState = fsm.ShoppingState()
            else:
                tempState = fsm.WorkState()

        if(self.thirst < baseStatThreshold and self.thirst < self.hunger*1.5):
            if(self.water > 0):
                tempState = fsm.DrinkState()
            elif(self.money >= 5):
                tempState = fsm.ShoppingState()
            else:
                tempState = fsm.WorkState()

        if(self.energy < baseStatThreshold and self.energy < self.hunger and self.energy < self.thirst):
            tempState = fsm.SleepState()

        if(self.happiness < baseStatThreshold and self.happiness < self.hunger and self.happiness < self.thirst and self.happiness < self.energy):
            tempState = fsm.SocialState()

        self.ChangeState(tempState)

    def CheckUrgency(self):
        urgent = False
        urgencyThreshold = 10
        if self.hunger < urgencyThreshold : urgent = True
        if self.thirst < urgencyThreshold : urgent = True
        if self.energy < urgencyThreshold : urgent = True
        if self.happiness < urgencyThreshold : urgent = True
        return urgent

    def ChangeState(self, newState):
        if(type(newState) == type(fsm.WorkState())):
            self.state = self.defaultWorkState
        else:
            self.state = newState
        if(type(self.state) != type(fsm.EatState()) and type(self.state) != type(fsm.DrinkState()) and type(self.state) != type(fsm.SleepState())):
            for i in ih.handler.GetInhabitantsAt(self.state):
                if(i.ID != self.ID):
                    self.SendMessage(i.ID, MsgEnum.GREET)

    def AddStats(self, money, hunger, thirst, energy, happiness):
        self.money += money
        if self.hunger < 100 - hunger : self.hunger += hunger
        if self.thirst < 100 - thirst : self.thirst += thirst
        if self.energy < 100 - energy : self.energy += energy
        if self.happiness < 100 - happiness : self.happiness += happiness

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
        print("")

    def SendMessage(self, rcvrID, contentChoice):
        if contentChoice == MsgEnum.GREET:
            content = "Hello there!"
        elif contentChoice == MsgEnum.GREET_BACK:
            content = "Obi Wan."
        elif contentChoice == MsgEnum.REQUEST_MEETING:
            content = "Do you wanna hang out?"
        elif contentChoice == MsgEnum.RESPOND_YES:
            content = "Let's do it right now!"
        elif contentChoice == MsgEnum.RESPOND_NO:
            content = "I need to do other stuff, sorry."
        msg = mh.Message(self.ID, rcvrID, content)
        mh.handler.HandleMsg(msg)
        
    def RcvMessage(self, msg):
        if(type(self.state) == type(fsm.SleepState())):
            print(self.ID, "is sleeping.") 
        elif(msg.content == "Hello there!"):
            self.SendMessage(msg.senderID, MsgEnum.GREET_BACK)
            self.AddStats(0, 0, 0, 0, +3)
        elif(msg.content == "Obi Wan."):
            self.AddStats(0, 0, 0, 0, +3)
        elif(msg.content == "Do you wanna hang out?"):
            if(self.CheckUrgency()):
                self.SendMessage(msg.senderID, MsgEnum.RESPOND_NO)
            else:
                self.SendMessage(msg.senderID, MsgEnum.RESPOND_YES)
                self.ChangeState(fsm.SocialState())
        elif(msg.content == "Let's do it right now!"):
            self.ChangeState(fsm.SocialState())
        #elif(msg.content == "I need to do other stuff, sorry."):

class MsgEnum(Enum):
    GREET = 1
    GREET_BACK = 2
    REQUEST_MEETING = 3
    RESPOND_YES = 4
    RESPOND_NO = 5
    #LEAVE = 6

