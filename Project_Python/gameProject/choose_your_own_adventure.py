name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You caome to a bridge, it looks wobble, do you want to cross it or head back(cross/back)? ").lower()
    
    if answer == "back":
        print("You go back and lose!")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        
        if answer == "yes":
            print("You tal to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. YOU LOSE!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
    
print(f"Thank you {name} for trying :)")