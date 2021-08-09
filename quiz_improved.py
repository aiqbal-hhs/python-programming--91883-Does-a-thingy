# Import modules - randomising
import time
import random

selection = 2, 3, 4, 5, 6, 7, 8, 9
random.shuffle(selection)
score = 0
loop = 0
userinput = ""
place = 0
num = selection[place]

# one in different languages
langone = "Tahi", "one", "uno", "vienas", "une", "unus", "ένας"

# question list
questions = "What is you name?", "Are we ready to start?", "Who is the king of the Greek titans?: \n Kronos, Zeus, Gaea, or Saturn", "The Romans invented the aqueduct?", "How many tasks does Hecules proform?", "The Roman god Cupid is the depiction of which Greek god?", "Tartarus, the prision of some Greek titans, is located where?: \n Mount Olympus, The underworld, Crete, or The garden of the Hesperides"  "Name one famous ancient Greek philosopher: \n", "Romans where and are known to steal and develop inventions, architecture, and more.\n What is one of the few things that they invented?", "What is the earliest form of recorded astronomy?"
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
answers = "yes", onea, twoa, threea, foura, fivea, sixa, sevena, eighta, ninea, tena

# correct statements
stateone = "Correct, Kronos is the father of the greek gods and king of the titans!"
statetwo = "Correct, the Romans are thought to have taken the idea from Babylonians, Egyptians, and Assyrians"
statethree = "Correct, Hercules was forced to do 2 more tasks after he recieved pay and help for them."
statefour = "Correct, He is the god of passion and fertility, \n and is sometimes considerred to be the male counterpart to his mother aphrodite!"
statefive = "Correct, it is the deepest pit in the underworld."
statesix = "That is correct, you know a philospher."
stateseven = "That is correct, that is one of their few inventions."
stateight = "That is correct, the babylonian's are the earliest recorded people to have used astronomy"
statenine = "That is correct, Romulus and his brother, Remus, founded Rome \n but Romulus killed his brother after the founding."
stateten = "That is correct, that is one of three ships that they primarily used."

# condensing the statements into one
statements = "zero", stateone, statetwo, statethree, statefour, statefive, statesix, stateseven, stateight, statenine, stateten

# asking name and welcome print - Quiz info and topic
name = input(questions[0])

print("Welcome to this quiz {}!".format(name))
time.sleep(0.5)
print("This quiz is about classical history, inolving mythology, science, and historical figures.")
print("This quiz was made by me, Oliver MacClure.")

time.sleep(3.333)

# loop ask start quiz
start = ""
while start != "yes":
    start = input(questions[1])
    start.strip()
    start.lower()
    if start == answers[0]:
        print("righty-O then, lets get started!")
    else:
        print("Okay, i'll wait.")
        time.sleep(5)

# easy Question asking loop
while loop != 8:
    if num == 4:
        userinput = int(input(questions[num]))
    else:
        userinput = input(questions[num])
    userinput = userinput.strip()
    userinput = userinput.lower()
    num -= 1
    if userinput in answers[num]:
        print(statements[num])
        print("You get {} point!".format(langone))
        score += 1
    else:
        print("Wrong, that wasn't the answer.")
    time.sleep(1)
    loop += 1
    place += 1
    num = selection[place]

loop = 0
num = random.randint(0, 1)

# Hard Question asking loop
while loop != 2:
    userinput = input(hardquestions[num])
    userinput = userinput.strip()
    userinput = userinput.lower()
    num += 9
    if userinput in answers[num]:
        print(statements[num])
        print("you get {} point!".format(langone))
        score += 1
    else:
        print("")
    time.sleep(1)
    loop += 1
    if num == 0:
        num += 1
    elif num == 1:
        num -= 1

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
