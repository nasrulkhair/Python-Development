print("Welcome to my computer quiz!")

#asking player to play or quit the game
playing = input("Do you want to play? ")


#conditionally check the input by user
if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")

#creating variable to collect score
score = 0
total_question = 0

#question 1
total_question += 1
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, It is incorrect :(")
 
#question 2
total_question += 1   
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, It is incorrect :(")
 
#question 3
total_question += 1   
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry, It is incorrect :(")

#question 4
total_question += 1    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Sorry, It is incorrect :(")
    
#question 5
total_question += 1    
answer = input("Siapa nama suami kamu? ")
if answer.lower() == "nasrul khair":
    print("Correct!")
    score += 1
else:
    print("Sorry, It is incorrect :(")
    
print("Congratulations!, you finished all the questions")
print(f"Your score is: {score}/{total_question} ({(score/total_question) * 100:.2f}%)")