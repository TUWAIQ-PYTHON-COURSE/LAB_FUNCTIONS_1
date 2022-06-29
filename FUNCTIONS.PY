def number(num):
    '''هذه الدالة كل سطر جديد تنقص عدد'''
    for i in range (num,0, -1):
        for x in range (i,0,-1):
            print(x, end = ' ')
        print()

number(5)
print(number.__doc__)