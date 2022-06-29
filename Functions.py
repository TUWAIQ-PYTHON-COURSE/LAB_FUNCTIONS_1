#[1]
def shape(num:int):
    ''' The function shape will print the numbers in hierarchically descending'''
    for i in range(0, num + 1):
        for j in range(num - i, 0, -1):
             print(j, end=' ')
        print()

shape(5)
