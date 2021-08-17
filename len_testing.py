
loop = 0
check = False

while loop != 11:
    while check is False:
        # ask input - then lower and remove spaces
        userinput = input("input a word: ")
        userinput = userinput.strip()
        userinput = userinput.lower()
        # checks if userinport has any number or letter
        if(len(userinput)):
            check = True
            print("correct")
        else:
            check = False
            print("nerd")
        loop += 1
    check = False
