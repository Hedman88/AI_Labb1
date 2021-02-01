import math
import sched, time
from inhabitant import Inhabitant
import fsm
import inhabitanthandler as ih

s = sched.scheduler(time.time, time.sleep)
updateTimer = 0
inhabitants = []

#Instantiate all inhabitants and start the loop
def main():
    inhabitants.append(Inhabitant(1, "Gustav", fsm.WorkAtQuarryState(), 0, 100))
    inhabitants.append(Inhabitant(2, "Olof", fsm.WorkAtQuarryState(), 30, 30))
    inhabitants.append(Inhabitant(3, "Pelle", fsm.WorkAtOfficeState(), 0, 100))
    inhabitants.append(Inhabitant(4, "Göran", fsm.WorkAtOfficeState(), 30, 30))
    ih.handler.inhabitants = inhabitants
    s.enter(1, 1, gameloop)

#Calls on Update() for every inhabitant
def gameloop():
    for i in range(len(inhabitants)):
        inhabitants[i].Update()
        if(type(inhabitants[i].state) == type(fsm.DeadState())):
            return
    s.enter(updateTimer, 1, gameloop)

main()
s.run()
