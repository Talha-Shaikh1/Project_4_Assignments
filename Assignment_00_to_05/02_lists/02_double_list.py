'''
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]
'''

def main():
    print("Welcome to our App :)")

    numbers: list[int] = [1,2,3,4,5]
    
    for number in range(len(numbers)):
        numbers[number] *= 2
    print(f"The doubled numbers are: {numbers}") # [2, 4, 6, 8, 10]

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()