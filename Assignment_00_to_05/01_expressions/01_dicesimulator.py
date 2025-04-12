'''
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
'''
import random

SIDES = 6

def die_roll():
    die1:int = random.randint(1, SIDES)
    die2:int = random.randint(1, SIDES)
    total:int = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")
    
def main():
    die1:int = 10
    print("die1 in main() start as "+ str(die1))
    die_roll()
    die_roll()
    die_roll()
    print("die1 in main() is "+ str(die1))
    
if __name__ == '__main__':
    main()