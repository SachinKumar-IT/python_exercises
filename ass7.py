#Ask the user for a temperature in Celsius (string input). Convert it to Fahrenheit, then calculate and print the temperature in Fahrenheit.

temp_celsius=input("Enter the temperature in Celsius:")
FahrenheitTemp = (float(temp_celsius) * (9/5)) + 32
print("The temperature in Fahrenheit is:", FahrenheitTemp)