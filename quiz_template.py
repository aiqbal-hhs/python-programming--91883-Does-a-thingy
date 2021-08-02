# Import modules and big variables
import time

score = 0

# asking name and welcome print
name = input("What is you name?")
print("Welcome to this quiz {}!".format(name))

# Quiz info and topic
print("This quiz is about classical history, inolving mythology, science, and historical figures.")
print("This quiz was made by me, Oliver MacClure.")

# loop ask start quiz
start = ""
while start != "yes":
    start = input("Are we ready to start?")
    start.strip()
    start.lower()
    if start == "yes":
        print("righty-O then, lets get started!")
    else:
        print("Okay, i'll wait.")
        time.sleep(5)

# First Question - Multi choice
print("Question one, Multiple choice")
firstq = input("""Who is the king of the Greek titans?
Kronos, Zeus, Gaea, or Saturn?
""")
firstq.strip()
firstq.lower()
    if firstq == "kronos" or firstq == "cronos" or firstq == "cronus":
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
secondq = input("The Romans invented the aqueduct?")
secondq.strip()
secondq.lower()
    if secondq == "false":
        print("Correct, the Romans are thought to have taken the idea from Babylonians, Egyptians, and Assyrians")
        score += 1
    elif secondq == "true":
        print("Incorrect, they have taken the idea from one of the countries they conquered.")
    else:
        print("I said 'True or False', how hard could it be!")

time.sleep(2)

# Third Question - Type the number
print("Question three, Type a Number")
thirdq = int(input("How many tasks does Hecules proform?"))
thirdq.strip()
thirdq.lower()
    if thirdq == 10:
        print("That is incorrect, It was the orignal number but it was changed.")
    elif thirdq == 12:
        print("Correct, Hercules was forced to do 2 more tasks after he recieved pay and help for them.")
        score += 1
    else:
        print("That is the worng number of tasks.")

time.sleep(2)

# Fourth Question - Write the answer
print("Question four, Geuss the answer")
fourthq = input("The Roman god Cupid is the depiction of which Greek god?")
fourthq.strip()
fourthq.lower()
    if fourthq == "eros":
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
fifthq = input("""Tartarus, the prision of some Greek titans, is located where?:
Mount Olympus, The underworld, Crete, or The garden of the Hesperides
""")
fifthq.strip()
fifthq.lower()
    if fifthq == "the underworld":
        print("Correct, it is the deepest pit in the underworld.")
        score += 1
    elif fifthq == "mount olympus":
        print("That is incorrect, mount olympus is the home of the gods.")
    elif fifth == "crete":
        print("""That is wrong,
crete is a greek island that was home to the wealthist
city-state of ancient greece at one point in time""")


