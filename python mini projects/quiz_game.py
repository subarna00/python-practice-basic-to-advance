print("Welcome to computer quix")

playing = input("Do you want to play\n >> ")

if playing.lower() != "yes":
    quit()
    
score = 0
while playing.lower() == "yes":
    print("==================================================")

    print("Let's play :)")

    answer = input("What does CPU stands for?\n >>")
    if answer.lower() == "cpu":
        print("Correct!") 
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does P stands for?\n >>")
    if answer.lower() == "p":
        print("Correct!") 
        score += 1
    else:
        print("Incorrect!")
    
    print("You scored:" + str(score))
    score = 0
    playing = input("Do you want to play again?\n >> ")