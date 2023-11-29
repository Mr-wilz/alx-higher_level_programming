#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    absolute_number = number * -1
    last_digit = (-1) * (absolute_number % 10)
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"The last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"The last digit of {number:d} is {last_digit:d} and is 0")
elif 0 < last_digit < 6:
    print(f"The last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
