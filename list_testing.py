x = 0

three = "three"
answer = "one", "two", three

while x < 5:
    firstq = input("list a number: ")
    firstq = firstq.strip()
    firstq = firstq.lower()
    if firstq in answer:
        print("working")
    else:
        print("fail")
    x += 1
