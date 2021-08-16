
loop = 0
check = False

while loop != 11:
    while check is False:
        # ask input - then lower and remove spaces
        userinput = input("input a word: ")
        userinput = userinput.strip()
        userinput = userinput.lower()
        if(len(userinput)):
            check = True
            print("gegegege")
        else:
            check = False
        loop += 1
    check = False
