'''
Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']
'''

def get_list_from_user():
    """Prompt the user to enter a list"""
    lst : str = []
    input_value: str = input("Enter the value of the list (or press Enter to finish): ")
    while input_value != '':
        lst.append(input_value)
        input_value = input("Enter the value of the list (or press Enter to finish): ")
    return lst

def main():
    print("Welcome to our App :)")
    
    lst: str = get_list_from_user()
    
    print(f"The list is: {lst}")
    
if __name__ == '__main__':
    main()