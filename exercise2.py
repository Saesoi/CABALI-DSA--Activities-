def calculateVoltage(current, resistance):
    return current * resistance

def calculateCurrent(voltage, resistance):
    return voltage / resistance

def calculateResistance(voltage, current):
    return voltage / current

def ohmsLawCalculator():
    print("What do you want to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        try:
            current = float(input("Enter the current (I) in amperes: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            voltage = calculateVoltage(current, resistance)
            print(f"The voltage is {voltage} volts")
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == "2":
        try:
            voltage = float(input("Enter the voltage (V) in volts: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            if resistance == 0:
                print("Resistance cannot be zero. Division by zero is not allowed.")
            else:
                current = calculateCurrent(voltage, resistance)
                print(f"The current is {current} amperes")
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == "3":
        try:
            voltage = float(input("Enter the voltage (V) in volts: "))
            current = float(input("Enter the current (I) in amperes: "))
            if current == 0:
                print("Current cannot be zero. Division by zero is not allowed.")
            else:
                resistance = calculateResistance(voltage, current)
                print(f"The resistance is {resistance} ohms")
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

ohmsLawCalculator()