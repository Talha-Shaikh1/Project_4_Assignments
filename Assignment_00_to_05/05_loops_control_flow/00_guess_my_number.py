'''
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48
'''

import random

my_number = random.randint(0, 99)

def main():
    print("I am thinking of a number between 0 and 99...") 
    guess = int(input("Enter a guess: "))
    
    while guess != my_number:
        if guess < my_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        guess = int(input("Enter a new number: "))
    print("Congrats! The number was:", my_number)
    
if __name__ == '__main__':
    main()