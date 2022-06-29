
def pyramid(num : int ) :
    ''' printing a pyramid number pattern starting from the received number and ending with 1 '''
    for i in range(0, num ):
        for j in range(num - i  , 0 , -1 ):
            print(j , end=" ")
        print()

pyramid(5)
print(pyramid.__doc__)




