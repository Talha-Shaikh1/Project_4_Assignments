'''
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
'''

def get_last_element(lst):
    """Print the last element in the list."""
    if lst:
        print(F"The last element of the list is '{lst[-1]}'")
    else:
        print("The list is empty.")

def get_list_from_user():
    """Prompt the user to enter a list"""
    lst : str = []
    input_value: str = input("Enter the value of the list (or 'done' to finish): ")
    while input_value.lower() != 'done':
        lst.append(input_value)
        input_value = input("Enter the value of the list (or 'done' to finish): ")
    return lst

def main():
    print("Welcome to our App :)")
    
    lst: str = get_list_from_user()
    
    print(f"The list is: {lst}")
    
    get_last_element(lst)
    
if __name__ == '__main__':
    main()  