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

name = input('what is your name?')
print('hi ' + name)
year = int(input('what year is it?'))
self_age = int(input('what is your age?')
father_age = int(input('how old is your father?'))
mother_age = int(input('how old is your mother?'))
early_year = year - self_age
late_year = early_year - 1


print('you were born in {} or {}. your father was {} when you were born and your mother was {}. your father is {} years older than your mother.'.format(early_year, late_year, father_born_age, mother_born_age, father_mother_age))
