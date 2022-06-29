
def printPattern( number : int ):
     rowsw = number
     for i in range(rowsw, 1, -1):
        for j in range(1, i + 1):
          print(j, end=' ')  
        print() 



printPattern(5)