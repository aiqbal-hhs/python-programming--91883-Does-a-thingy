import random
loop = 0
pep = ""
x = random.randint(0, 1)

things = "opple", "tanana", "thear", "frape", "firange", "sineapple"
three = "three"
answer = "one", "two", three, "four", "five", "six"

easyorder = random.sample(range(0, 8), 8)
hardorder = random.sample(range(0, 2), 2)
print(easyorder)
print(hardorder)

print(random.choice(things))

while loop < 30:
    x = random.randint(0, 1)
    print(things[x])
    loop += 1
loop = 0

langone = "Tahi", "one", "uno", "vienas", "une", "unus", "ένας"

print("Correct, you get {} point!".format(langone))

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist[1])

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [1, 1, 1], k = 3))

while loop != 10:
    pep = input(things[x])
    pep = pep.lower()
    pep = pep.strip()
    if pep in answer[x]:
        print("Working!")
    else:
        print("Error!")
    loop += 1
    x = random.randint(0, 5)
