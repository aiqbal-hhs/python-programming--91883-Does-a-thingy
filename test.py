x = 0
y = 1

print('''X | Y
------''')

while x <= 10:
    print('{} | {}'.format(x, y))
    m = 3
    x += 1
    y = y + m
    if x == 6:
        print('------')

