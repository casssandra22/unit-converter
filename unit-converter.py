def convert_length(value, from_unit, to_unit):
    # Convert to meters first
    if from_unit == "feet":
        meters = value * 0.3048
    elif from_unit == "inches":
        meters = value * 0.0254
    else:
        meters = value
    
    # Convert from meters to desired unit
    if to_unit == "feet":
        return meters / 0.3048
    elif to_unit == "inches":
        return meters / 0.0254
    else:
        return meters

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    else:
        return value

def convert_weight(value, from_unit, to_unit):
    # Convert to kilograms first
    if from_unit == "pounds":
        kg = value * 0.453592
    elif from_unit == "ounces":
        kg = value * 0.0283495
    else:
        kg = value
    
    # Convert from kilograms to desired unit
    if to_unit == "pounds":
        return kg / 0.453592
    elif to_unit == "ounces":
        return kg / 0.0283495
    else:
        return kg

def main():
    print("Welcome to the Unit Converter!")
    while True:
        print("\nChoose conversion type:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue
        
        value = float(input("Enter the value to convert: "))
        
        if choice == '1':
            from_unit = input("Enter the unit to convert from (meters/feet/inches): ").lower()
            to_unit = input("Enter the unit to convert to (meters/feet/inches): ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        
        elif choice == '2':
            from_unit = input("Enter the unit to convert from (celsius/fahrenheit): ").lower()
            to_unit = input("Enter the unit to convert to (celsius/fahrenheit): ").lower()
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        
        elif choice == '3':
            from_unit = input("Enter the unit to convert from (kilograms/pounds/ounces): ").lower()
            to_unit = input("Enter the unit to convert to (kilograms/pounds/ounc