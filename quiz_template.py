# Import modules and big variables
import time

score = 0

questions = "What is you name?", "Are we ready to start?", "Who is the king of the Greek titans?: Kronos, Zeus, Gaea, or Saturn", "The Romans invented the aqueduct?", "How many tasks does Hecules proform?", "The Roman god Cupid is the depiction of which Greek god?", "Tartarus, the prision of some Greek titans, is located where?: Mount Olympus, The underworld, Crete, or The garden of the Hesperides"  "Name one famous ancient Greek philosopher:", "Romans where and are known to steal and develop concepts, inventions, architecture, and more. What is one of the few things that they invented?", "What is the earliest form of recorded astronomy?"
hardquestions = "Who is the founder of Rome?", "Name one ship that the Romans primarily used:"

qonea = "kronos", "cronos", "cronus"
qtwoa = "false"
qthreea = 12
qfoura = "eros"
qfivea = "the underworld"
qsixa = "socrates", "socrate", "plato", "aristotle", "thale", "pythagoras", "democritus", "empedokles", "anaxagoras", "anaximander", "epicurus"
qsevena = "concrete", "concreet", "underfloor heating", "heating", "house heating"
qeighta = "babylonian", "babylon"
qninea = "romulus", "romulus and remus", "remus and romulus"
qtena = "trireme", "quadrireme", "quinquereme"

answers = qonea, qtwoa, qthreea, qfoura, qfivea, qsixa, qsevena, qeighta, qninea, qtena

# asking name and welcome print
name = input(questions[0])
print("Welcome to this quiz {}!".format(name))

# Quiz info and topic
print("This quiz is about classical history, inolving mythology, science, and historical figures.")
print("This quiz was made by me, Oliver MacClure.")

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

# First Question - Multi choice
print("Question one, Multiple choice")
firstq = input(questions[2])
firstq.strip()
firstq.lower()
    if firstq in answers[0]:
        print("Correct, Kronos is the father of the greek gods and king of the titans!")
        score += 1
    elif firstq == "zeus":
        print("Wrong, Zeus is the king of the Greek gods.")
    elif firstq == "gaea":
        print("Wrong, Gaea is Mother Earth, she gave birth to the titans.")
    elif firstq == "saturn":
        print("Wrong, Saturn is the Roman depiction of him.")
    else:
        print("Thats not an answer I told you!")

time.sleep(2)

# Second Question - True or False
print("Question two, True or False")
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
print("Question three, Type a Number")
thirdq = int(input(questions[4]))
thirdq.strip()
thirdq.lower()
    if thirdq == 10:
        print("That is incorrect, It was the orignal number but it was changed.")
    elif thirdq in answers[2]:
        print("Correct, Hercules was forced to do 2 more tasks after he recieved pay and help for them.")
        score += 1
    else:
        print("That is the worng number of tasks.")

time.sleep(2)

# Fourth Question - Write the answer
print("Question four, Geuss the answer")
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
print("Question five, Multiple choice")
fifthq = input(questions[6])
fifthq.strip()
fifthq.lower()
    if fifthq in answers[4]:
        print("Correct, it is the deepest pit in the underworld.")
        score += 1
    elif fifthq == "mount olympus":
        print("That is incorrect, mount olympus is the home of the gods.")
    elif fifth == "crete":
        print("""That is wrong,
crete is a greek island that was home to the wealthist
city-state of ancient greece.""")
    elif fifthq == "the garden of hesperides":
        print("That is incorrect, that is Hera's orchard which is found near portugal")
    else:
        print("Thats not one of the answers")

time.sleep(2)

# Sixth Question - multi answer typing
print("Question six, type the answer")
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
print("Question seven, type the answer")
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
print("Question eight, type the answer")
eighthq = input(questions[9])
eighthq.strip()
eighthq.lower()
    if eighthq in answers[7]:
        print("That is correct, the babylonian's are the earlisr recorded people to have used astronomy")
        score += 1
    else:
        print("")

time.sleep(2)

# ninth question - hardcore question - multi choice
print("Question nine, hardcore question, multiple choice")
ninthq = input(hardquestions[0])
ninthq.strip()
ninthq.lower()
    if ninthq in answers[8]:
        print("That is correct, Romulus and his brother, Remus, founded Rome but Romulus killed his brother after the founding.")
        score += 1
    else:
        print("thats wrong, thats not who founded rome, or may not them alone.")

time.sleep(2)

# tenth question - hardcore question - type the answer
print("Question ten, hardcore question, type the answer")
tenthq = input(hardquestions[1])
tenthq.strip()
tenthq.lower()
    if seventhq in answers[9]:
        print("That is correct, that is one of three ships that they primarily used.")
        score += 1
    else:
        print("that is incorrect, thats not one of the ships they used.")

time.sleep(2)
