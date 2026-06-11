#2. Unit Conversion: Write a program that takes a temperature input in Celsius and converts it into Fahrenheit, Kelvin, and Rankine. Display all results in a clear, formatted table.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
rankine = (celsius + 273.15) * 9/5

print("\nTemperature Conversion")
print("-------------------------")
print("Celsius     =", celsius)
print("Fahrenheit  =", fahrenheit)
print("Kelvin      =", kelvin)
print("Rankine     =", rankine)
