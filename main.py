import math
from inhabitant import Inhabitant
from fsm import WorkState

def main():
    inhabitants = []
    print("How many people do you want to simulate?")
    for i in range(int(input())):
        print(i)
        inhabitants.append(Inhabitant(i+1, "Test Subject", WorkState()))

    while(True):
        for i in range(len(inhabitants)):
            inhabitants[i].Update()
            inhabitants[i].PrintStats()

main()
