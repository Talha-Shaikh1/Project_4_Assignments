'''
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
'''

def main():
    print("Welcome to our App :)")
    
    # Constant values
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    # Calculate the number of seconds in a year
    second_in_year = SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_YEAR

    print(f"There are {second_in_year} seconds in a year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()