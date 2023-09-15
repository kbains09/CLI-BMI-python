def calculate_bmi(weight_lb, height_ft, height_in):
    # Convert height to inches
    height_total_in = (height_ft * 12) + height_in

    # Calculate BMI
    bmi = (weight_lb / (height_total_in ** 2)) * 703
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
weight_lb = float(input("Enter your weight in pounds: "))
height_ft = int(input("Enter your height in feet: "))
height_in = int(input("Enter your height in inches: "))

# Calculate BMI
bmi = calculate_bmi(weight_lb, height_ft, height_in)

# Interpret BMI and display the result
print(f"Your BMI is: {bmi:.2f}")
interpretation = interpret_bmi(bmi)
print(f"You are in the '{interpretation}' category.")
