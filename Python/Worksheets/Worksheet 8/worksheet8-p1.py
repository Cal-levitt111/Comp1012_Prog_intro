import random

print("*** FizzBuzz Game with Computer ***")
print("*** Count from 1 to 100 ***\n")

for i in range(0, 101):

    if i % 3 == 0 and i % 5 == 0:
        expected_in = "FizzBuzz"
    elif i % 3 == 0:
        expected_in = "Fizz"
    elif i % 5 == 0:
        expected_in = "Buzz"
    else:
        expected_in = str(i)

    