pwd = input("What is the master password? ")

#defining function
def view():
    #open the file and select the mode (a/r/w)
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.strip("|")
            print(f"User: {user}, Password: {passw}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    #open the file and select the mode (a/r/w)
    with open("password.txt","a") as f:
        f.write(f"{name} | {pwd}\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue