# importing random number generator
import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


#generating random number and store into a variable
random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print(f"You guessed the correct number: {random_number}")
        break

    elif user_guess > random_number:
        print("Your guess were above the number")
    else:
        print("You got it wrong :(")
        print("Your guess were below the number")
        
        
        
print(f"Total guesses made are: {guesses}")