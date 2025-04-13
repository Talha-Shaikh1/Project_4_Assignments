'''
Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92

Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

value = random.randint(1, 6)
'''
import random

def main():
    print("Welcome to our App :)")
    
    # Generate and print 10 random numbers in the range 1 to 100
    for i in range(10):
        random_number = random.randint(1, 100)
        print(f"{i + 1}: '{random_number}'", end=" ")
    print()  # Print a newline after the loop
    
    
        
if __name__ == '__main__':
    main()