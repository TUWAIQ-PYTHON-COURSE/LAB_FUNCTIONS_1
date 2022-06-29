num = int(input("Enter number: "))

def tringle():
    '''it drows a tringle from the number you choose to 1'''
    for x in range(0, num):
        for y in range(num - x, 0, -1):
            print(y, end =' ')
        print()
tringle()

print(tringle.__doc__)