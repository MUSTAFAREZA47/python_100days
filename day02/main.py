# two_digit_number = input("Write any two digit number?\n")
#
# sum_two_digit_number = int(two_digit_number[0]) + int(two_digit_number[1])
#
# print(sum_two_digit_number)


# BMI CALCULATOR

# print("Calculate your BMI !!!")
#
# weight = input("What is your weight in kg?\n")
# height = input("What is your height in meter?\n")
#
# bmi = float(weight) / (float(height) ** 2)
#
# print("Your BMI is " + bmi)

# TIP CALCULATOR

print("Welcome to the tip calculator !!!")

total_bill = float(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

number_of_people = int(input("How many people to split the bill?\n"))

billed_per_person = round((total_bill + tip)/number_of_people, 2)

print(f"Each person should pay: ${billed_per_person}")



