'''
We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

You make a guess, saying your number is either higher than or lower than the computer's number

If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

These steps make up one round of the game. The game is over after all rounds have been played.

We've provided a sample run below.
'''
import random



print("Welcome to high low Game!")
print(f"{'-' * 30}")

score = 0

def play_game(round_num):
    global score
    print("Round ",round_num)
    user = int(input("Enter your number: "))
    computer_num = random.randint(1, 100)
    user_guess = input("Is your number higher or lower than the computer's? (higher/lower): ")
    if user_guess.lower() == "lower" and user < computer_num:
        print(f"You were right the computer's num was {computer_num}")
        score += 1
        print(f"Your score is now {score}")    
    elif user_guess.lower() == "higher" and user > computer_num:
        print(f"You were right the computer's num was {computer_num}")
        score += 1
        print(f"Your score is now {score}") 
    else:
        print(f"You were wrong the computer's num was {computer_num}")
        print(f"Your score is now {score}") 
        

def main():
    for i in range(1, 6):
        play_game(i)
        i+= 1
    print(f"Game Over! Your final score is {score}")
    
if __name__ == "__main__":
    main()