import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]
#options = options[0]
#print(options)

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Please enter a valid option :)")
        continue
    
    random_number = random.randint(0,2)
    # rock - 0, paper - 1, scissors - 2
    computer_pick = options[random_number]
    print(f"Computer pick, {computer_pick}." )
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1
    elif user_input == computer_pick:
        print("Its a draw!")
        user_score += 1
        computer_score += 1
    else:
        print("You lost :(")
        computer_score += 1

print(f"You won, {user_score} times.")
print(f"Computer won, {computer_score} times.")
print("Goodbye")
    