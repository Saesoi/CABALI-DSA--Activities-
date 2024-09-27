def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperatureConverter():
    temperature = float(input("Enter a temperature: "))
    conversion_type = input("Do you want to convert:\nA. Celsius to Fahrenheit\nB. Fahrenheit to Celsius\n")

    if conversion_type == "A":
        result = celsiusToFahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")
    elif conversion_type == "B":
        result = fahrenheitToCelsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")
    else:
        print("Invalid selection. Please enter 1 or 2.")

temperatureConverter()