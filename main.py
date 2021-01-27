import math
from inhabitant import Inhabitant
import fsm

def main():
    inhabitants = []
    print("How many people do you want to simulate?")
    for i in range(int(input())):
        print(i)
        inhabitants.append(Inhabitant(i+1, "Test Subject", fsm.WorkAtQuarryState()))

    while(True):
        for i in range(len(inhabitants)):
            inhabitants[i].Update()
        if(type(inhabitants[0].state) == type(fsm.DeadState())):
           break

main()
