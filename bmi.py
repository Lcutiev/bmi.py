# Convert weight_lb to kilograms:
weight_lb = int(input("Please enter your weight in pounds: "))
weight_kg = weight_lb * 0.454592
# Convert height_in to m:
height_in = int(input("Please enter your height in inches: "))
height_m = height_in * 0.0254

# Caculate the BMI: bmi
bmi = weight_kg/height_m**2
print(bmi)

# Print out bmi
if (bmi > 40):
    print("Obesity Class 3")
elif(35 <= bmi < 40):
    print("Obesity Class 2 ")
elif(35 <= bmi < 40):
    print("Obesity Class 1")
elif(25 <= bmi < 30):
    print("Overweight")
elif(18.5 <= bmi < 25):
    print("Normal weight")
elif(17 <= bmi < 18.5):
    print("Underweight Class 1")
elif(16 <= bmi < 17):
    print("Underweight Class 2")
else:
    print("Underweight Class 3")