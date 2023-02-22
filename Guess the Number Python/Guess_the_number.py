import random

while True:
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

    # select a number randomly with limit of upper and lower in parameter and store it in variable
    random_number = random.randint(lower_limit, upper_limit)
    print("You will have to choose a number between ", lower_limit, " and ", upper_limit)

    # Assign a variable "chances" that will act as the counter for a loop
    chances = 0
    while chances < 8:
        chances += 1
        guess = int(input("Enter your guess: "))
        if random_number == guess:
            print("Congratulations, you did it. The number was ", random_number)
            break
        elif guess < random_number:
            print("You guessed a small number.")
        elif guess > random_number:
            print("You guessed a large number.")
        if chances == 7:
            print("\n You've run out of chances")
            print("\n The number was ", random_number)
            print("Better luck next time")
            break
    print("\n")
    break
