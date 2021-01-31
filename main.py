import math
import sched, time
from inhabitant import Inhabitant
import fsm
import messagehandler as mh
import inhabitanthandler as ih

s = sched.scheduler(time.time, time.sleep)
inhabitants = []

def main():
    #print("How many people do you want to simulate?")
    #for i in range(int(input())):
    #    if(i < 2):
    #        inhabitants.append(Inhabitant(i+1, "Test Subject", fsm.WorkAtQuarryState()))
    #    else:
    #        inhabitants.append(Inhabitant(i+1, "Test Subject", fsm.WorkAtOfficeState()))
    inhabitants.append(Inhabitant(1, "Gustav", fsm.WorkAtQuarryState(), 0, 100))
    inhabitants.append(Inhabitant(2, "Olof", fsm.WorkAtQuarryState(), 30, 30))
    inhabitants.append(Inhabitant(3, "Pelle", fsm.WorkAtOfficeState(), 0, 100))
    inhabitants.append(Inhabitant(4, "Göran", fsm.WorkAtOfficeState(), 30, 30))
    ih.handler.inhabitants = inhabitants
    #inhabitants[0].SendMessage(2, "Hello there")
    s.enter(1, 1, gameloop)

def gameloop():
    for i in range(len(inhabitants)):
        inhabitants[i].Update()
        if(type(inhabitants[i].state) == type(fsm.DeadState())):
            return
    s.enter(0, 1, gameloop)

main()
s.run()
