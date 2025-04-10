def main():
    print("Welcome to our App! :)")
    length_1: int = int(input("Enter the length of side 1: "))
    length_2:int = int(input("Enter the length of side 2: "))
    length_3:int = int(input("Enter the length of side 3: "))
    
    print(f"The perimeter of the triangle is {length_1 + length_2 + length_3}.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()