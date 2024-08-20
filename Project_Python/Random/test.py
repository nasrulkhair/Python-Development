# Exercise 1
name = input("Enter your name: ")
print("Your name is: ", name)

# Exercise 2
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = int(hours) * float(rate)
print("Pay: ", pay)

# Try/Except structure
astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
    
print("Firts ", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
    
print("Second ", istr)

#example 2
rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except: 
    ival = -1
    
if ival > 0:
    print("Nice job!")
else:
    print("Not a number.")
    
# Exercise 1
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
hours = int(hours)
rate = float(rate)

if hours >= 40:
    hours_extra = hours - 40
    extra_pay = hours_extra * 1.5 * rate
    pay = (hours * rate) + extra_pay
else:
    pay = hours * rate

print("Pay: ", pay)
    
    
#FUNCTION Exercise

def salary(hours, rate):
    if hours >= 40:
        hours_extra = hours - 40
        extra_pay = hours_extra * 1.5 * rate
        pay = (hours * rate) + extra_pay
        
    else:
        pay = hours * rate
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
hours = int(hours)
rate = float(rate)

print("Your salary is: ", salary(hours, rate))


# While Loop
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# Counting in a loop
#Finding average using loop
count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)

# filtering in a loop
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large number", value)
print("After")

# Seaching Using a Boolean variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

#example: find the samllest number

smallest = None
print("Before", smallest)
for value in [9, 41, 12, 3, 74,]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

# Exercise: Take the following Python code that stores a string: 
str = "X-DSPAM_Confidence: 0.8475   "
e = str.find(":")
s = str[e+1:].strip()  # Extract the substring after ':' and strip any leading/trailing whitespace
print(s)