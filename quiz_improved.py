# Import modules - randomising numbers - variables
import time
import random

selection = 4, 2, 3, 11, 6, 10, 8, 9, 5, 7
preshuffle = list(selection)
random.shuffle(preshuffle)
selection = tuple(preshuffle)
place = 0
num = selection[place]
check = False
score = 0
loop = 0
userinput = ""
selectone = random.randint(0, 7)

# one in different languages
langone = "Tahi", "One", "Uno", "Vienas", "Une", "Unus", "ένας"

# question list
nameq = "What is your name? \n"
startq = "Are we ready to start? \n"
firsq = "Who's the king of the Greek Titans?:\nKronos, Zeus, Gaea, or Saturn\n"
secondq = "True or False: The Romans invented the aqueduct? \n"
thirdq = "How many tasks does Hecules proform? \n"
fourthq = "The Roman god Cupid is the depiction of which Greek god? \n"
fifthq = """Tartarus is located where?:
Mount Olympus, The Underworld, Crete, or Africa
"""
sixthq = "Name one famous ancient Greek philosopher: \n"
seventhq = """Romans are known to steal, then develop
inventions, architecture, and more.
What is one of their inventions? \n"""
eigthq = "What is the earliest form of recorded astronomy? \n"
ninthq = "Who is the founder of Rome? \n"
tenthq = "Name one ship that the Romans primarily used: \n"

# Stacko taco questo
questions = [nameq, startq, firsq, secondq, thirdq, fourthq]
otherhalf = [fifthq, sixthq, seventhq, eigthq, ninthq, tenthq]
questions.extend(otherhalf)

# answer list
onea = "kronos", "cronos", "cronus"
twoa = "false"
threea = "12"
foura = "eros"
fivea = "the underworld", "underworld", "under world"
sixa = ["socrates", "socrate", "plato", "aristotle", "thale", "pythagoras"]
sixb = ["democritus", "empedokles", "anaxagoras", "anaximander", "epicurus"]
sixa.extend(sixb)
sevena = "concrete", "underfloor heating", "heating", "house heating"
eighta = "babylonian", "babylon"
ninea = "romulus", "romulus and remus", "remus and romulus"
tena = "trireme", "quadrireme", "quinquereme"

# stack all answers together
answers = ["yes", onea, twoa, threea, foura, fivea]
answers2 = sixa, sevena, eighta, ninea, tena
answers.extend(answers2)

# correct statements
stateone = "Kronos is the father of the greek gods and king of the titans!"
statetwo = """People think romans took the idea
from Babylonians, Egyptians, and Assyrians"""
statethree = """Hercules was forced to do 2 more tasks
to replace the ones he recieved pay or help for."""
statefour = """He is the god of passion and fertility
and is sometimes considerred to be the male counterpart
to his mother aphrodite!"""
statefive = "It is the holding place of monsters and some greek titans."
statesix = "You know a philospher."
stateseven = "That is one of their few inventions."
stateight = "The earlist form of astronomy comes from babylonians"
statenine = "Romulus and Remus founded Rome \n but Romulus soon killed remus."
stateten = "That is one of three ships that they primarily used."

# condensing the statements into one
statements = ["zero", stateone, statetwo, statethree, statefour]
statement = statefive, statesix, stateseven, stateight, statenine, stateten
statements.extend(statement)

# end of the set up
# Start of the quiz

# asking name and welcome print - provide Quiz info and topic
name = input(questions[0])

print("Welcome to this quiz {}!".format(name))
time.sleep(0.5)
print("This quiz is about classical history")
print("It inolves mythology, science, and historical figures.")
print("This quiz was made by Oliver MacClure.")

time.sleep(3)

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

# Question asking loop
# Check loop number under 10
while loop != 10:
    # this while loop is looking for if the answer is blank
    while check is False:
        # ask input - then remove spaces and lowering letters
        userinput = input(questions[num])
        userinput = userinput.strip()
        userinput = userinput.lower()
        # lower var num to check answer - I have one less answer than question
        num -= 1
        # this if is cheacking if userinput is empty
        if(len(userinput)):
            check = True
            # checks if userinput is one of the answers for that question
            if userinput in answers[num]:
                # when the answer is correct this code will run
                print("Correct, {}".format(statements[num]))
                print("You get {} point!".format(langone[selectone]))
                selectone = random.randint(0, 7)
                score += 1
            else:
                # when the answer is wrong this code will run
                print("Wrong, that wasn't the answer.")
        # this else is for if there is an empty userinput
        else:
            check = False
    # this is for after the checking for answer and input
    time.sleep(1)
    loop += 1
    # this checks if the loop is lower than 10
    # the code breaks if [place] excedes 9
    if loop != 10:
        place += 1
        num = selection[place]
    check = False

# End of quiz - Scoring and responce
# sets respon acording to score
if score == 0:
    respon = "Maybe you should study some classics sometime."
elif score >= 1 and score <= 3:
    respon = "You did well, not first or last, a nice spot. study a little. :)"
elif score >= 4 and score <= 6:
    respon = "it's not too bad, it shows that you know something."
elif score >= 7 and score <= 9:
    respon = "WOW! thats like really really good!"
elif score == 10:
    respon = "Damn, well, umm, Congratulations! You've earned it! :)"
# this is for if someone gets more than 10 or less than 0
else:
    respon = "How did you do it, you big cheater?"
# Gives user score and responce
print(respon, "\n you got {} points".format(score))
