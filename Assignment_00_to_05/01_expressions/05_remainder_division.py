"""
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2
"""

def main():
    print("Welcome to our app! :)")
    print("This app will divide two numbers and show the result of the division and the remainder.")
    
    # collect input from the user
    num_1 = int(input("Please enter an integer to be divided: "))
    num_2 = int(input("Please enter an integer to divide by: "))
    
    remainder = num_1 % num_2
    result = num_1 // num_2
    
    print(f"The result of this division is {result} with a remainder of {remainder}.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()