import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lets = int(input("How many letters?\n"))
nums = int(input("How many numbers?\n"))
syms = int(input("How many symbols?\n"))


# WITH POSSIBILITY OF REPETITION
# Eazy Level - Order not randomised:     e.g. 4 letter, 2 symbol, 2 number = JduE&!91
yourPassEasy = []
for i in range(lets):
    yourPassEasy += letters[random.randint(0, len(letters) - 1)]
for i in range(nums):
    yourPassEasy += numbers[random.randint(0, len(numbers) - 1)]
for i in range(syms):
    yourPassEasy += symbols[random.randint(0, len(symbols) - 1)]
    
print(f"Your easy pass: {''.join(yourPassEasy)}")


# WITH POSSIBILITY OF REPETITION
# Hard Level - Order of characters randomised:    create the sequence and then, scramble the indexes with random     e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
yourPassHard = []
yourPassHard.extend(yourPassEasy)
random.shuffle(yourPassHard)

print(f"Your hard pass: {''.join(yourPassHard)}")


# WITH POSSIBILITY OF REPETITION
# EVEN HARDER LEVEL
passEvenHarder = []

passSize = int(input("How big do you want your pass?\n"))
lets = int(input("How many letters?\n"))
nums = int(input("How many numbers?\n"))
syms = int(input("How many symbols?\n"))

# adding everything according to their amounts to one only list
randomScope = []

randomLets = []
for i in range(lets):
    randomLets += letters[random.randint(0, len(letters) - 1)]

randomNums = []
for i in range(nums):
    randomNums += numbers[random.randint(0, len(numbers) - 1)]

randomSyms = []
for i in range(syms):
    randomSyms += symbols[random.randint(0, len(symbols) - 1)]

randomScope.extend(randomLets)
randomScope.extend(randomNums)
randomScope.extend(randomSyms)


while len(passEvenHarder) < passSize:
    item = randomScope[random.randint(0, len(randomScope) - 1)]
    passEvenHarder += item
    randomScope.remove(item)

print(f"Your hard-ass password is: {''.join(passEvenHarder)}")




