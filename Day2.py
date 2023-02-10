two_digit_number = input("Type a two digit number: ")

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num + second_num)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) // float(height)**2
print(int(bmi))


age = input("What is your current age? ")
age_left = 90 - int(age) 

days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")