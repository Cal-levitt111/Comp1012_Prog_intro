num1 = int(input("Please enter a whole number"))
num2 = int(input("Please enter another whole number"))
sum = 0

while num1 >= num2:
    print("Please make sure your first number is smaller than the second")
    num1 = int(input("Please re-enter your first num"))
    num2 = int(input("Please re-enter a larger whole number"))


for i in range(num1, num2 + 1):
    sum += i

print(sum)
