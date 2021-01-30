import math
import sched, time
from inhabitant import Inhabitant
import fsm
import messagehandler as mh
import inhabitanthandler as ih

s = sched.scheduler(time.time, time.sleep)
inhabitants = []

def main():
    print("How many people do you want to simulate?")
    for i in range(int(input())):
        print(i)
        if(i < 2):
            inhabitants.append(Inhabitant(i+1, "Test Subject", fsm.WorkAtQuarryState()))
        else:
            inhabitants.append(Inhabitant(i+1, "Test Subject", fsm.WorkAtOfficeState()))
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
