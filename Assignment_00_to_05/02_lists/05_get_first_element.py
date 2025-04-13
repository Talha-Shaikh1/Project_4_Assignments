
'''
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
'''

def get_first_element(lst):
    """Print the first element in the list."""
    if lst:
        print(F"The first element of the list is {lst[0]}")
    else:
        print("The list is empty.")
        
def get_list_from_user():
    """Prompt the user to enter a list of numbers."""
    lst : str = []
    input_value: str = input("Enter the alue of the list (or 'done' to finsih): ")
    while input_value.lower() != 'done':
        lst.append(input_value)
        input_value = input("Enter the value of the list (or 'done' to finish): ")
    return lst

def main():
    print("Welcome to our App :)")
    
    lst: str = get_list_from_user()
    
    print(f"The list is: {lst}")
    
    get_first_element(lst)

if __name__ == '__main__':
    main()