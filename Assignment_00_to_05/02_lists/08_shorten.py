'''
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

'''

MAX_LENGTH: int = 3

def shorten(lst: list):
    """Remove dlements from the until the list is MAX_LENGTH items long."""
    while len(lst) > MAX_LENGTH:
        removed_item: str = lst.pop()
        print(f"Removed '{removed_item}' from the list.")
    print(f"The final list is: {lst}")
    
def get_list_from_user():
    """Prompt the user to enter a list"""
    lst : str = []
    input_value: str = input("Enter the value of the list (or press 'Enter' to finish): ")
    while input_value != '':
        lst.append(input_value)
        input_value = input("Enter the value of the list (or press 'Enter' to finish): ")
    return lst

def main():
    print("Welcome to our App :)")
    
    lst: str = get_list_from_user()
    if not lst:
        print("The list is empty.")
        return
    elif len(lst) <= MAX_LENGTH:
        print(f"The list is already shorter than {MAX_LENGTH} items.")
        print(f"The list is: {lst}")
        return
    print(f"The list is: {lst}")
    shorten(lst)
    
if __name__ == '__main__':
    main()