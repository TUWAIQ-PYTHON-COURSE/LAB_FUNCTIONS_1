def numbers(num):
    ''' This function takes an integer number and returns sequence of numbers started from the given number to zero'''

    for i in range(0, num,):
        for x in range(num-i,0, -1):
            print(x, end = ' ')
        print()
                       
num = 5
numbers(num)
print(numbers.__doc__)