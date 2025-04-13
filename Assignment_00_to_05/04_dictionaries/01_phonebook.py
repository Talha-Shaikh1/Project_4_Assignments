# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def create_phonebook():
    phonebook = {}
    while True:
        name = input("Enter a name (or press 'enter' to finish): ").lower()
        if name == '':
            break
        phone_number = input("Enter the phone number: ")
        phonebook[name] = phone_number
    return phonebook

def display_phonebook(phonebook):
    print("Phonebook:")
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")
        
def lookup_number(phonebook):
    name = input("Enter a name to look up: ")
    if name.lower() in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")
        
def main():
    phonebook = create_phonebook()
    display_phonebook(phonebook)
    lookup_number(phonebook)
    
if __name__ == "__main__":
    main()