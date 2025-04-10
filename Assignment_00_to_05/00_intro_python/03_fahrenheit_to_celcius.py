def main():
    print("Fahrenheit to Celcius! :)")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celcius = (fahrenheit - 32) * 5 / 9
    print(f"The temperature in Celcius is: {celcius:.2f}°C")
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()