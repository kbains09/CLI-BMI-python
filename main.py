def calculate_bmi(weight, height, unit_system):
    if unit_system == "metric":
        bmi = weight / (height ** 2)
    elif unit_system == "imperial":
        bmi = (weight / (height ** 2)) * 703
    else:
        print("Invalid unit system. Please use 'metric' or 'imperial'.")
        return None
    
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Get user input
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
unit_system = input("Enter 'metric' for kilograms and meters or 'imperial' for pounds and inches: ").lower()

# Calculate BMI
bmi = calculate_bmi(weight, height, unit_system)

# Interpret BMI and display the result
if bmi is not None:
    print(f"Your BMI is: {bmi:.2f}")
    interpretation = interpret_bmi(bmi)
    print(f"You are in the '{interpretation}' category.")
