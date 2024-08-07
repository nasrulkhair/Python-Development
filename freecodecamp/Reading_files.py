fh = open("mbox-short.txt")
print(fh)

line_count = 0
for line in fh:
    line = line.strip()
    line_count = line_count + 1
    print(line.upper())
    
print(f"Total number of lines: {line_count}")


#Example of list method
stuff = []
stuff.append("book")
stuff.append(99)
stuff.append("biskut")


#x = stuff.pop()
stuff.insert(1,"air")
#print(x)
print(stuff)

# List with while loop

numlist = []
while True:
    inp = input("Enter your number: ")
    if inp == "done":
        break
    value = int(inp)
    numlist.append(value)
print(numlist)
average = sum(numlist) / len(numlist)
print("Average: ", average)

#example dictonary
counts = {"quincy": 1,"murgesh": 42, "beau": 100, "0":10}
print(counts.get("kris", 0))

#exmample 2 dictionary
def nama(names):
    counts = {}
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    return counts

print(nama(["a","b","c","a","b"]))

# example 3
counts = {}
names = ["a","b","c","a","b"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#counting words in text
counts = {}
print("Enter a line of text: ")
line = input("")


words = line.split()
print(words)
#kena loop 1-1 dalam list untuk jadikan lower case
words = [word.lower() for word in words]

print("Words: ", words)

print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts:", counts)

#example
jjj = {"quincy": 1,"murgesh": 42, "beau": 100, "nas":10}
for a,b in jjj.items():
    print(a,b) 
    
# Example Regular Expresion 

import re
hand = open("mbox-short.txt")
print(hand)
nulist = []
for line in hand:
    line = line.strip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    nulist.append(num)
print("Maximum: ", max(nulist))