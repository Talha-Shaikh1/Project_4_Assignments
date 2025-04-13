# Write a function that takes a list of numbers and returns the sum of those numbers.


def main():
    print("Welcome to our App :)")

    numbers: int = [1, 2, 3, 4, 5]
    total: int = 0
    for num in numbers:
        total += num
    print(f"The sum of the numbers is: {total}")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()