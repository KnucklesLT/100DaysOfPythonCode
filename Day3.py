number = int(input("Which number do you want to check? "))

if (number % 2):
    print("This is an odd number.")
else:
    print("This is an even number.")

# BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap year checker
year = int(input("Which year do you want to check? "))

if (year % 4 == 0):
    if (year % 400 == 0):
        print("Leap year.")
    elif (year % 100 == 0):
        print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


#pizza calculator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size.lower() == 's':
    bill += 15
elif size.lower() == 'm':
    bill += 20
elif size.lower() == 'l':   
    bill += 25
else:
    print("Pizza size incorrectly entered.")

if add_pepperoni.lower() == 'y':
  if size.lower() == 's':
    bill += 2
  else:
    bill += 3

if extra_cheese.lower() == 'y':
    bill += 1

print(f"Your final bill is: ${bill}.")


# Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

love_score = 0
true_score = 0
for el in 'true':
    for letter in name1.lower():
        if el == letter:
            true_score+=1
    for letter in name2.lower():
        if el == letter:
            true_score+=1

for el in 'love':
    for letter in name1.lower():
        if el == letter:
            love_score+=1
    for letter in name2.lower():
        if el == letter:
            love_score+=1

total_score = int(str(true_score) + str(love_score))
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")