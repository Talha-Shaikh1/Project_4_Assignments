'''
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
'''

numbers = []
def get_num_input_from_user():
    
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        
        number = int(user_input)
        numbers.append(number)
    return numbers

def count_numbers(numbers:list):
    number_dict = {}
    for number in numbers:
        if number in number_dict:
            number_dict[number] += 1
        else:
            number_dict[number] = 1
    return number_dict

def print_number_count(number_dict:dict):
    for number, count in number_dict.items():
        print(f"{number} appears {count} times.")
        
def main():
    get_num_input_from_user()
    number_dict = count_numbers(numbers)
    print_number_count(number_dict)
    
if __name__ == "__main__":
    main()