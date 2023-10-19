import random
correct = False
guesses =  0
number = random.randint(0, 100)

while correct is not True and guesses < 5:
    guess = int(input("Please input your guess"))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    elif guess == number:
        print("Congratualtions you win!")
        correct = True
    
    guesses += 1

if guesses == 5:
    print("Sorry you ran out of guesses, better luck next time!")
    print("The number was", number)