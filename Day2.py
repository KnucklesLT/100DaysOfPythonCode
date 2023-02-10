two_digit_number = input("Type a two digit number: ")

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num + second_num)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) // float(height)**2
print(int(bmi))