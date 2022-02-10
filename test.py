x = 0
y = 1

print('''X | Y
------''')

while x <= 15:
    print('{} | {}'.format(x, y))
    m = 3
    x += 1
    y = y + m
    if x == 6:
        print('------')

true = False
numberstart = int(input('what is a good number between 0 and 10,000?'))
while true == False:
    if numberstart >= 0.0000001:
        numberstart *= 1.2 ** 4 
        print(numberstart)
    elif numberstart == inf:
        true = True
    else:
        true = True
else:
    print("kaboom")
