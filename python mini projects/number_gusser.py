import random

top_of_range = input("Enter a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter number greater than 0 next time.")
        quit()
else:
    print("Please enter number next time.")
    quit()

gusses = 0
ramdom_number = random.randint(0,top_of_range)
while True:
    gusses += 1
    user_guess = input("Guess a number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Print enter number next time.")
        continue

    if user_guess == ramdom_number:
        print("You got it!")
        print("You made it in",gusses,"guesses")
        break
    elif user_guess > ramdom_number:
        print("You were above the number")
    else:
        print("You were below the number")