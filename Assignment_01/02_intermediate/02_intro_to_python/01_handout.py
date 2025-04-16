'''
A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

Ingenuity on the surface of Mars (source: NASA)

When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.
'''

def main():
    # Constants for gravity on different planets
    MERCURY_GRAVITY = 0.376 
    VENUS_GRAVITY = 0.889 
    MARS_GRAVITY = 0.378 
    JUPITER_GRAVITY = 2.36 
    SATURN_GRAVITY = 1.081 
    URANUS_GRAVITY = 0.815 
    NEPTUNE_GRAVITY = 1.14 
    EARTH_GRAVITY = 1.0
    
    weight_on_earth = float(input("Enter the weight on Earth: "))
    planet = input("Enter the planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ").strip().lower()
    if planet == "mercury":
        weight_on_planet = weight_on_earth * MERCURY_GRAVITY
    elif planet == "venus":
        weight_on_planet = weight_on_earth * VENUS_GRAVITY
    elif planet == "mars":
        weight_on_planet = weight_on_earth * MARS_GRAVITY
    elif planet == "jupiter":
        weight_on_planet = weight_on_earth * JUPITER_GRAVITY
    elif planet == "saturn":
        weight_on_planet = weight_on_earth * SATURN_GRAVITY
    elif planet == "uranus":
        weight_on_planet = weight_on_earth * URANUS_GRAVITY
    elif planet == "neptune":
        weight_on_planet = weight_on_earth * NEPTUNE_GRAVITY
    else:
        print("Invalid planet name.")
        return
    
    # Round the result to 2 decimal places
    weight_on_planet = round(weight_on_planet, 2)
    print(f"Your weight on {planet.capitalize()} is: {weight_on_planet} kg")
    
    
if __name__ == "__main__":
    main()