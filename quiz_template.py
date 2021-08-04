# Import modules - randomising
import time
import random

easyorder = random.sample(range(0, 8), 8)
hardorder = random.sample(range(0, 2), 2)
print(easyorder)
print(hardorder)

score = 0
loop = 0
userinput = ""

# one in different languages
langone = "Tahi", "one", "uno", "", "",

# question list
questions = "What is you name?", "Are we ready to start?", "Who is the king of the Greek titans?: Kronos, Zeus, Gaea, or Saturn", "The Romans invented the aqueduct?", "How many tasks does Hecules proform?", "The Roman god Cupid is the depiction of which Greek god?", "Tartarus, the prision of some Greek titans, is located where?: Mount Olympus, The underworld, Crete, or The garden of the Hesperides"  "Name one famous ancient Greek philosopher:", "Romans where and are known to steal and develop inventions, architecture, and more. What is one of the few things that they invented?", "What is the earliest form of recorded astronomy?"
hardquestions = "Who is the founder of Rome?", "Name one ship that the Romans primarily used:"

# answer list
onea = "kronos", "cronos", "cronus"
twoa = "false"
threea = 12
foura = "eros"
fivea = "the underworld"
sixa = "socrates", "socrate", "plato", "aristotle", "thale", "pythagoras", "democritus", "empedokles", "anaxagoras", "anaximander", "epicurus"
sevena = "concrete", "concreet", "underfloor heating", "heating", "house heating"
eighta = "babylonian", "babylon"
ninea = "romulus", "romulus and remus", "remus and romulus"
tena = "trireme", "quadrireme", "quinquereme"

# stack all answers together
answers = onea, twoa, threea, foura, fivea, sixa, sevena, eighta, ninea, tena

# asking name and welcome print - Quiz info and topic
name = input(questions[0])
print("Welcome to this quiz {}!".format(name))

print("This quiz is about classical history, inolving mythology, science, and historical figures.")
print("This quiz was made by me, Oliver MacClure.")

time.sleep(3)

# loop ask start quiz
start = ""
while start != "yes":
    start = input(questions[1])
    start.strip()
    start.lower()
    if start == "yes":
        print("righty-O then, lets get started!")
    else:
        print("Okay, i'll wait.")
        time.sleep(5)

# Question asking loop
while loop != 10:
    userinput = input(random.choice(questions))
    userinput = userinput.strip()
    userinput = userinput.lower()
    if userinput in answers:
        print("Correct, you get {} point!".format(langone))







# first question multi choice
userinput = input(questions[2])
userinput = userinput.strip()
userinput = userinput.lower()
    if userinput in answers[0]:
        print("Correct, Kronos is the father of the greek gods and king of the titans!")
        score += 1
    elif userinput == "zeus":
        print("Wrong, Zeus is the king of the Greek gods.")
    elif userinput == "gaea":
        print("Wrong, Gaea is Mother Earth, she gave birth to the titans.")
    elif userinput == "saturn":
        print("Wrong, Saturn is the Roman depiction of him.")
    else:
        print("Thats not an option I gave you!")

time.sleep(2)

# Second Question - True or False
secondq = input(questions[3])
secondq.strip()
secondq.lower()
    if secondq in answers[1]:
        print("Correct, the Romans are thought to have taken the idea from Babylonians, Egyptians, and Assyrians")
        score += 1
    elif secondq == "true":
        print("Incorrect, they have taken the idea from one of the countries they conquered.")
    else:
        print("I said 'True or False', how hard could it be!")

time.sleep(2)

# Third Question - Type the number
thirdq = int(input(questions[4]))
thirdq.strip()
thirdq.lower()
    if thirdq == 10:
        print("That is incorrect, it was the orignal number of tasks but it was changed.")
    elif thirdq in answers[2]:
        print("Correct, Hercules was forced to do 2 more tasks after he recieved pay and help for them.")
        score += 1
    else:
        print("That is the worng number of tasks.")

time.sleep(2)

# Fourth Question - Write the answer
fourthq = input(questions[5])
fourthq.strip()
fourthq.lower()
    if fourthq in answers[3]:
        print("""Correct, He is the god of passion and fertility,
              and is sometimes considerred to be the male counterpart to his mother aphrodite!""")
        score += 1
    elif fourthq == "aphrodite":
        print("That is wrong, but you were close (it's one of her children).")
    else:
        print("That is incorrect, additionally Cupid is not a baby but a full grown man.")

time.sleep(2)

# Fifth Question - Multi choice
fifthq = input(questions[6])
fifthq.strip()
fifthq.lower()
    if fifthq in answers[4]:
        print("Correct, it is the deepest pit in the underworld.")
        score += 1
    elif fifthq == "mount olympus":
        print("That is incorrect, mount olympus is the home of the gods.")
    elif fifthq == "crete":
        print("""That is wrong,
crete is a greek island that was home to the wealthist
city-state of ancient greece.""")
    elif fifthq == "the garden of hesperides":
        print("That is incorrect, that is Hera's orchard which is found near portugal")
    else:
        print("Thats not one of the answers")

time.sleep(2)

# Sixth Question - multi answer typing
sixthq = input(questions[7])
sithq.strip()
sithq.lower()
    if sixthq in answers[5]:
        print("That is correct, you know a philospher.")
        score += 1
    else:
        print("Sorry but I haven't heard of them.")

time.sleep(2)

# seventh question - guess the invention
seventhq = input(questions[8])
seventhq.strip()
seventhq.lower()
    if seventhq in answers[6]:
        print("That is correct, that is one of their few inventions.")
        score += 1
    else:
        print("That is wrong, they did not invent that.")

time.sleep(2)

# eighth question - type the answer
eighthq = input(questions[9])
eighthq.strip()
eighthq.lower()
    if eighthq in answers[7]:
        print("That is correct, the babylonian's are the earliest recorded people to have used astronomy")
        score += 1
    else:
        print("That is incorrect, thats not the earliest civilization")

time.sleep(2)

# Hard questions - Start
print("Get ready because the hard questions are starting.")

# ninth question - hardcore question - multi choice
ninthq = input(hardquestions[0])
ninthq.strip()
ninthq.lower()
    if ninthq in answers[8]:
        print("That is correct, Romulus and his brother, Remus, founded Rome but Romulus killed his brother after the founding.")
        score += 1
    else:
        print("thats wrong, thats not who founded rome, or maybe not them alone.")

time.sleep(2)

# tenth question - hardcore question - type the answer
tenthq = input(hardquestions[1])
tenthq.strip()
tenthq.lower()
    if seventhq in answers[9]:
        print("That is correct, that is one of three ships that they primarily used.")
        score += 1
    else:
        print("that is incorrect, thats not one of the ships they used.")

time.sleep(2)

# End of quiz - Scoring and responce

    if score == 0:
        responce = "Maybe you should study some classics sometime."
    elif score >= 1 and score <= 3:
        responce = "You did well, not first or last, a nice spot. If you want higher though, study a little. : )"
    elif score >= 4 and score <= 6:
        responce = "Thats not too bad, it shows that you know somethings, congratulations."
    elif score >= 7 and score <= 9:
        responce = "WOW! thats like really really good!"
    else score == 10:
        responce = "Damn, well you sure know your stuff. Congratulations! You've earned it! : )"
