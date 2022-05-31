#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number < 0):
    lastDigit = (-number) % 10
else:
    lastDigit = number % 10
if(lastDigit > 5):
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastDigit))
elif(lastDigit == 0):
    print("Last digit of {} is {} and is 0".format(number, lastDigit))
elif(lastDigit < 6):
    if(lastDigit != 0):
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, lastDigit))
