x = 0

three = "three"
four = "four"
addin = [three, four]
answer = ["one", "two"]
answer.extend(addin)

while x < 5:
    firstq = input("list a number: ")
    firstq = firstq.strip()
    firstq = firstq.lower()
    if firstq in answer:
        print("working")
    else:
        print("fail")
    x += 1
