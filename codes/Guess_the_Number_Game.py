print("Guss the number game between 1 to 100")
import random
number = random.randint(1,100) 
guess = None
count = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    count += 1
    if guess == number:
        print("Congratulations! You guessed the number in", count, "attempts")
    elif guess < number:
        print("You guessed too low")
    else:
        print("You guessed too high")