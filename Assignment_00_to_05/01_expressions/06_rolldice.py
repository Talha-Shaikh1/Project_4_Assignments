'''
Simulate rolling two dice, and prints results of each roll as well as the total.
'''
import random

def main():
    print("Welcome to our App :)")
    
    SIDES=6
    die_1 = random.randint(1, SIDES)
    die_2 = random.randint(1, SIDES)
    total = die_1 + die_2
    
    print(f"Die 1: {die_1}")
    print(f"Die 2: {die_2}")
    print(f"Total: {total}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()