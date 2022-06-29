
def printPattern( number : int ):
    ''' This function takes one number then print the numbers that lead the number in upside parmiad '''
    rowsw = number
    for i in range(rowsw, 1, -1):
        for j in range(1, i + 1):
          print(j, end=' ')  
        print() 



printPattern(5)

print(printPattern.__doc__)

