'''
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
'''

def main():
    print("Welcome to our App! :)")
    # collect input from user
    feet: float = float(input("Type a number of feet to convert to inches: "))
    # convert feet to inches
    inches: float = feet * 12.0
    # output the result
    print(f"{feet} feet is {inches} inches")
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()