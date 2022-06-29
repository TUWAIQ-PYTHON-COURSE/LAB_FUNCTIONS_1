
### Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

def exm(n1 : int) -> int :
    '''here we use for to ring numbers with new line'''

    for i in range (n1,  0, -1):
        for j in range (i, 0, -1):
            print(j, end = ' ')
        print('\n')
exm(5)

print(__doc__)